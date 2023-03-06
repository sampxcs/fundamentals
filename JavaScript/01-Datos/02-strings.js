'use strict'

const title = 'Curso de JavaScript'
const text = 'hola mundo'
const description = 'En este curso vas a aprender todo lo necesario para programar en "JavaScript"'

// Con (``) se pueden acceder a variables dentro de un string

console.log(`${title} ${text}`) // Se colocan `` y las variables van dentro de ${}

// Puedes acceder a los indices de un string usando []
// y el numero de indice al que se quiere acceder

// Los indices empiezan en "0"
console.log(text[3]) // Corresponde a la letra "s"

/* ----------- METODOS DE STRINGS ------------ */

// .length devuelve la longitud de un string
console.log('length:', text.length) // 10

// toUpperCase() Devuelve el string en MAYUSCULAS
console.log('toUpperCase:', text.toUpperCase()) // HOLA MUNDO

// toLowerCase() Devuelve el string en minusculas
console.log('toLowerCase():', text.toLowerCase()) // hola mundo

// capitalize() Primera letra en MAYUSCULAS y el resto en minusculas
console.log('capitalize():', text) // Hola mundo

/*
// capitalize() Primera letra de cada palabra en MAYUSCULAS
console.log("title():", text.title())  // Hola Mundo

// strip() Elimina los espacios a los lados
console.log("strip():", text.strip())  // hola mundo

// lstrip() Elimina los espacios a la izquierda
console.log("lstrip():", text.lstrip())  // hola mundo

// rstrip() Elimina los espacios a la derecha
console.log("rstrip():", text.rstrip())  // hola mundo

// find() Busca la palabra y devuelve el indice donde empieza
console.log("find():", text.find("mundo"))  // 5

// rfind() Busca y devuelve el indice donde termina
console.log("rfind():", text.rfind("mundo"))  // 10

// replace() Reemplaza la palabra 1 por la 2
console.log("replace():", text.replace("mundo", "nikki"))  // hola nikki

// in Busca la palabra y devuelve un booleano
console.log("in:", "mundo" in text)  // True

// not in Busca si NO esta palabra y devuelve un booleano
console.log("not in:", "mundo" not in text)  // False

// count() Devuelve el numero de veces que se repite "hola"
console.log("count():", text.count("hola"))  // 1

// startswith() Devuelve TRUE si el string EMPIEZA con "hola"
console.log("startswith():", text.startswith("hola"))  // True

// endswith() Devuelve TRUE si el string TERMINA con "hola"
console.log("endswith():", text.endswith("hola"))  // False

// isdigit() Determinan si los caracteres del string son dígitos
console.log("isdigit():", text.isdigit())  // False */
