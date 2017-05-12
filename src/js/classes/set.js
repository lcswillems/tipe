// u_n = random
function random_1d(nbs) {
	var set = []
	for (var i = 0; i < nbs; i++) {
		set.push(Math.random())
	}
	return [[0, 1], set]
	
}

// u_n = (random, random)
function random_2d(nbs) {
	var set = []
	for (var i = 0; i < nbs; i++) {
		set.push([Math.random(), Math.random()])
	}
	return [[0, 1], [0, 1], set]
}

// u_n = n*a mod 1
// où a est irrationnel
function nb1_mult_mod_1(nbs, num, den) {
	var set = []
	for (var i = 0; i < nbs; i++) {
		set.push(((i*num)/den)%1)
	}
	return [[0, 1], set]
}

// u_n = (n*a mod 1, n*b mod 1)
// où a et b sont irrationnels
function nbs2_mult_mod_1(nbs, num1, den1, num2, den2){
	var set = []
	for (var i = 0; i < nbs; i++) {
		set.push([((i*num1)/den1)%1, ((i*num2)/den2)%1])
	}
	return [[0, 1], [0, 1], set]
}

// u_n = abs(cos(n))
function abs_cos_n(nbs) {
	var set = []
	for (var i = 0; i < nbs; i++) {
		set.push(Math.abs(Math.cos(i)) % 1)
	}
	return [[0, 1], set]
}

// z_(n+1) = A*z_n
// où z_n = (x_n, y_n) et A est une matrice 2x2
function gen_alea_plan(nbs, A, z) {
	var set = []
	for (var i = 0; i < nbs; i++) {
		set.push([z[0]%1, z[1]%1])
		z = [A[0][0]*z[0] + A[0][1]*z[1], A[1][0]*z[0] + A[1][1]*z[1]] 
	}
	return [[0, 1], [0, 1], set]
}

// x_(n+1) = a*x_n+c
// où a et c sont des entiers
function gen_alea_lin(nbs, a, c, m, x) {
	var set = []
	var y = new BigInteger(x)
	for (var i = 0; i < nbs; i++) {
		set.push(y.remainder(m).toJSValue())
		y = y.multiply(a).add(c)
		console.log(y.remainder(m).toJSValue())
	}
	return [[0, m], set]
}

// u_n = (a^n mod 10^k)/10^k
// où a et k sont des entiers
function last_power_digits(nbs, a, k) {
	var set = []
	var seq = 1, pow10 = Math.pow(10, k)
	for (var i = 0; i < nbs; i++) {
		set.push(seq/pow10)
		seq = (seq*a)%pow10
	}
	return [[0, 1], set]
}