
// Note: Non null assertion operator(!) tells compiler that value typed as optional can't be null
const App: Element = document.querySelector("#app")!

const Button: HTMLButtonElement = document.createElement("button")!
Button.innerHTML = `Button`;
Button.id = "12";


for (let _index = 0; _index < 10; _index++) {
    App.appendChild(Button);
}

console.log(App);
