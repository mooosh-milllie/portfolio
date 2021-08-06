// document.addEventListener("DOMContentLoaded", loadText)
// let xhr = new XMLHttpRequest()

// function loadText(params) {

//     // xhr.open("Get", "text.txt", true);

//     // xhr.onload = function () {
//     //     if (this.status === 200) {
//     //         console.log(this.responseText)
//     //     }
//     // }

//     // xhr.send();

//     console.log(window.innerWidth)
// }
unsortedList = [{'first_element' : 4}, {'second_element': 6}, {'third_element': 2 }]
sortedList = [];

// for(let i = 0; i < unsortedList.length; i++) {
//     console.log(i)
// }
let newArr = [];
unsortedList.forEach( tupleis => {
    let a = Object.values(tupleis)
    console.log(a)
    return newArr.push(a)
    //console.log(a)
});

newArr.sort((a, b) => a-b)



console.log(newArr)

console.log(window.innerWidth)