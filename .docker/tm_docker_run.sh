#!/bin/bash

tm_docker_run() {
	local debug="false"
	local display="host.docker.internal:0"
	local dryrun="false"
	local entrypoint=""
	local globus="false"
	local image=""
	local local=""
	local name=""
	local registry="docker.io/"
	local remote="/root/local_mount/"
	local usage="$FUNCNAME [-h] [-e \"entrypoint\"] [-i <image>] [-l <local path to mount>] [-R <registry>] [-r <remote path to mount>]
	-- opens a temporary Docker container with a self contained version of CMSSW

	where:
		-D [display]          set the display (default: ${display})
		-d                    print the command that will be run, but don't execute it (default: ${dryrun})
		-e [entrypoint]       specify the entrypoint, if not the default (default: ${entrypoint})
		-g                    mount the local globus folder (default: ${globus})
		-h                    show this help text
		-i [image]            specify the Docker image to be used (default: ${image})
		-l [local path]       local path to mount in container (default: ${local})
		-n [container name]   to keep the container after this run, specify the container name (default: ${name})
		-R [registry]         the Docker registry of the image (default: ${registry})
		-r [remote path]      remote path to mount in the container (default: ${remote})
		-v                    print extra debugging information (default: ${debug})

	example: treemaker_docker -l `pwd` -r /home/cmsusr/workdir"

	local OPTIND OPTARG
	while getopts 'D:de:ghi:l:n:R:r:v' option; do
		case "$option" in
			D) display=$OPTARG
			   ;;
			d) dryrun="true"
			   ;;
			e) entrypoint=$OPTARG
			   ;;
			g) globus="true"
			   ;;
			h) echo "$usage"
			   return 0
			   ;;
			i) image=$OPTARG
			   ;;
			l) local=$OPTARG
			   ;;
			n) name=$OPTARG
			   ;;
			R) registry=$OPTARG
			   ;;
			r) remote=$OPTARG
			   ;;
			v) debug="true"
			   ;;
			:) echo "missing argument for -$OPTARG" >&2
			   echo "$usage" >&2
			   return -1
			   ;;
			\?) echo "illegal option: -$OPTARG" >&2
				echo "$usage" >&2
				return -2
				;;
		esac
	done
	shift $((OPTIND - 1))

	# Format the local mount point
	if [[ "$local" != "" ]]; then
	local local_mount="-v ${local}:${remote}"
	fi

	# Format the image used
	if [[ -z ${image} ]]; then
		if [[ "${registry: -1}" == "/" ]]; then
			registry="${registry: : -1}"
		fi
		if [[ "${registry}" == *"docker.io"* ]]; then
			image=${registry}/treemaker/treemaker:Run2_2017-standalone
		elif [[ "${registry}" == *"gitlab-registry.cern.ch"* ]]; then
			image=${registry}/treemaker/treemaker/treemaker:Run2_2017-standalone
		fi
	fi

	# Only do the xhost checking if the system has xhost
	if [[ $(command -v xhost) ]] && [[ ! "${dryrun}" == "true" ]]; then
		# Capture the output of the xhost command and look for the lines:
		#  "access control enabled, only authorized clients can connect"
		#  "INET:localhost
		# If the first is different, then the xhost access should be reset by doing:
		#  xhost -
		# Then check again. If either the second line is missing, or the first was there, but the second one was missing, then do:
		#  xhost +127.0.0.1
		# Then check again. If it's not right this time, then exit and throw an error
		xhost_enabled="access control enabled, only authorized clients can connect"
		xhost_localhost="INET:localhost"
		xhost_check="$(xhost)"
		if [[ $xhost_check == *"${xhost_localhost}"* ]]; then
			echo "Note: access control already enabled, including an opening for localhost"
		else
			xhost -
			xhost_check="$(xhost)"
			if [[ $xhost_check != *"${xhost_enabled}"* ]]; then
				xhost +127.0.0.1
				xhost_check="$(xhost)"
				if [[ $xhost_check != *"${xhost_localhost}"* ]]; then
					echo "ERROR: Unable to set the xhost settings properly"
					return -3
				fi
			fi
		fi
	fi

	cmd="docker run --rm -it -e DISPLAY=${display}"
	if [[ "${globus}" == "true" ]]; then
		cmd="${cmd} -v ~/.globus:/home/cmsusr/.globus"
	fi
	if [[ -n $local_mount ]]; then
		cmd="${cmd} ${local_mount}"
	fi
	if [[ -n ${name} ]]; then
		cmd=${cmd// --rm/}
		cmd="${cmd} --name ${name}"
	fi
	if [[ -n ${entrypoint} ]]; then
		cmd="${cmd} --entrypoint ${entrypoint}"
	fi
	cmd="${cmd} ${image}"
	
	if [[ "${debug}" == "true" ]]; then
		set -x
	fi
	if [[ "${dryrun}" == "true" ]]; then
		echo "${cmd}"
	else
		eval ${cmd}
	fi
	set +x

	return 0
}
