/* Graph class */

function Graph(canvas) {
	var self = this

	self.canvas = canvas
	self.context = self.canvas[0].getContext("2d")
}

Graph.prototype.size = function(width, divisions){
	this.width = width
	this.xDivisions = divisions
}

Graph.prototype.draw = function(set){
	var window = set.slice(0, -1)
	var values = set.slice(-1)[0]

	var depth = window.length

	var xMin = window[0][0], xMax = window[0][1]
	this.canvas[0].width = this.width

	if (depth == 1) {
		var yMin = 0, yMax = 1
		this.height = this.width / 5
		this.yDivisions = 1
	} else {
		var yMin = window[1][0], yMax = window[1][1]
		this.height = this.width*((yMax - yMin)/(xMax-xMin))
		this.yDivisions = this.xDivisions
	}

	this.canvas[0].height = this.height
	this.context.clearRect(0, 0, this.canvas[0].width, this.canvas[0].height)

	var xStep = (xMax - xMin)/this.xDivisions
	var xPixel = this.width/this.xDivisions
	var yStep = (yMax - yMin)/this.yDivisions
	var yPixel = this.height/this.yDivisions

	var stats = []
	for (var i = 0; i < this.xDivisions*this.yDivisions; i++) {
		stats.push(0)
	}

	for (var i = 0; i < values.length; i++) {
		var e = values[i]
		if (depth == 1) {
			e = [e, 0]
		}
		stats[parseInt(e[0]/xStep) + this.xDivisions*parseInt(e[1]/yStep)] += 1
	}

	var statsTotal = values.length
	var statsMax = 0
	for (var i = 0; i < stats.length; i++) {
		statsMax = Math.max(statsMax, stats[i])
	}

	for (var i = 0; i < stats.length; i++) {
		var intensity = parseInt(stats[i]/statsMax * 255)
		this.context.fillStyle="rgb("+intensity+","+intensity+","+intensity+")"
		this.context.fillRect((i%this.xDivisions)*xPixel, parseInt(i/this.xDivisions)*yPixel, xPixel, yPixel)
	}

	// Test du Khi²
	// T = \sum (Y_s - N*P_s)^2/(N*P_s)
	// Ici : T = (\sum (Y_s - N/n)^2)/(N/n)

	var statsAverage = values.length / stats.length
	var sum = 0
	for (var i = 0; i < stats.length; i++) {
		sum += Math.pow(stats[i] - statsAverage, 2)
	}
	var statsKhi2 = sum/statsAverage

	this.canvas.data({'total': statsTotal, 'max': statsMax, 'index': statsKhi2})
}

/*
- Rajouter les axes
*/