const input = document.querySelector("input");
const neuralBackground = document.querySelector("#neuralBackground");

const network = new brain.NeuralNetwork();
network.train([
	{input: { r: 1, g: 1, b: 1}, output: { light: 1 }},
	{input: { r: 0, g: 0, b: 0}, output: { dark: 1 }},
	{input: {r: 1, g: 0.99, b: 0}, output: { light: 1 }},
	{input: {r: 1, g: 0.07, b: 0}, output: { dark: 1 }},
	{input: {r: 1, g: 0.6, b: 0}, output: { dark: 1 }},
	{input: {r: 0, g: 1, b: 0.06}, output: { light: 1 }},
	{input: {r: 0, g: 0.3, b: 1}, output: { dark: 1 }},
	{input: {r: 0, g: 0.7, b: 1}, output: { dark: 1 }},
])

input.addEventListener("change", (e) => {
	console.log(e.target.value)
	const rgb = getRgb(e.target.value);
	console.log(rgb);
	neuralBackground.style.background = e.target.value;

	const result = brain.likely(rgb, network);
	console.log(result);
	neuralBackground.style.color = result === "dark" ? "white" : "black"
});

getRgb = (hex) => {
	var shorthandRegex = /^#?([a-f\d])([a-f\d])([a-f\d])$/i;
	hex = hex.replace(shorthandRegex, function(m, r, g, b) {
	  return r + r + g + g + b + b;
	});

	var result = /^#?([a-f\d]{2})([a-f\d]{2})([a-f\d]{2})$/i.exec(hex);
	return result ? {
	  r: Math.round(parseInt(result[1], 16) / 2.55) / 100,
	  g: Math.round(parseInt(result[2], 16) / 2.55) / 100,
	  b: Math.round(parseInt(result[3], 16) / 2.55) / 100,
	} : null;
}