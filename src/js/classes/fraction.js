/* Fraction class */

function Fraction(num, den) {
	this.num = num
	this.den = den
	this.reduce()
}

Fraction.prototype.reduce = function() {
	function gcd(a, b) { return (b == 0) ? a : gcd(b, a%b) }
	d = 1
	this.num = this.num/d
	this.den = this.den/d
}

Fraction.prototype.add = function(fraction) {
	return new Fraction(this.num*fraction.den + this.den*fraction.num, this.den*fraction.den)
}

Fraction.prototype.sub = function(fraction) {
	return new Fraction(this.num*fraction.den - this.den*fraction.num, this.den*fraction.den)
}

Fraction.prototype.mult = function(fraction) {
	return new Fraction(this.num*fraction.num, this.den*fraction.den)
}

Fraction.prototype.div = function(fraction) {
	return new Fraction(this.num*fraction.den, this.den*fraction.num)
}

// Fraction.prototype.decimal = function(nbs) {
// 	var num = this.num % this.den, den = this.den
// 	return num/den
// }