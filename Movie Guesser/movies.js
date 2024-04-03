//js file for ponyo

function getRandomInt(max) {

    return Math.floor(Math.random() * max)

    }

var ponyoArray = []

for (let i = 1; i <= 46; i++) {
        
    if (i <10) {
        ponyoArray.push('Ponyo_Pics/Ponyo_00' + i + '.jpg')
    }

    if (i > 9) {
        ponyoArray.push('Ponyo_Pics/Ponyo_0' + i + '.jpg')
    }
}

//log-----------
console.log(ponyoArray)

console.log(getRandomInt(23))


//rand print----------------------------------------------
let ponyoRandom = getRandomInt(46)

for (let i = 1; i <= 46; i++) {

    if (ponyoRandom == i) {
        document.write('<img id="img" src="' + ponyoArray[i] + '">')
    
    }
}

//----------------------------------HMC----------------------------------------------------------------------------

/* 
var HMCArray = []

for (let i = 1; i <= 46; i++) {
        
    if (i <10) {

        HMCArray.push("HMC_Pics/Howl's_Moving_Castle_00" + i + '.jpg')
    }

    if (i > 9) {

        HMCArray.push("HMC_Pics/Howl's_Moving_Castle_0" + i + '.jpg')
    }
}




//log-----------
console.log(HMCArray)

console.log(getRandomInt(55))


//rand print----------------------------------------------

let HMCRandom = getRandomInt(55)

for (let i = 1; i <= 55; i++) {

    if (HMCRandom == i) {
        document.write('<img id="img" src="' + HMCArray[i] + '">')
    
    }
}
 */