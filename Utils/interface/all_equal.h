#ifndef all_equal_h
#define all_equal_h

namespace utils {
	// check is multiple values are equal
	// taken from: https://stackoverflow.com/questions/15208831/check-to-see-if-all-variable-are-equal-to-the-same-value-in-c
	template<typename T, typename U>
	inline bool all_equal(T&& t, U&& u) {
		return (t == u);
	}

	template<typename T, typename U, typename... Ts>
	inline bool all_equal(T&& t, U&& u, Ts&&... args) {
		return (t == u) && all_equal(u, std::forward<Ts>(args)...);
	}
}

#endif
