def printGetPyDictHeader(file):

    header = ["# format for dict entries:\n",
              "#                                                data: [0, ['sample'] , []]\n",
              "#                                                  MC: [1, ['sample'] , []]\n",
              "#                               MC w/ extended sample: [1, ['sample','sample_ext'] , []]\n",
              "#                   MC w/ negative weights (amcatnlo): [1, ['sample'] , [neff]]\n",
              "# MC w/ negative weights (amcatnlo) + extended sample: [1, ['sample','sample_ext'] , [neff, neff_ext]]\n",
              "\n",
              "flist = [\n"
              ]
    file.writelines(header)
