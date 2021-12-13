//Let's start by creating 2 different variables. The first will represent the original alphabet in the original language, stored as one large string. And the second will represent the new shifted alphabet based on the 'n' shift parameter. That value will be empty by default.
var alphabet = "abcdefghijklmnopqrstuvwxyz";
var newalpha = "";

//Now let's setup a function to create the newly shifted alphabet.
function shift(n){
	for (let i = 0; i < alphabet.length; i++){
		let offset = (i + n) % alphabet.length;
		newalpha += alphabet[offset];
	}
}
//The algorithm essentially looks ahead by 'n' characters and it wraps around back to the beginning once it reaches the end of the alphabet.
//This will give you the new alphabet to work with for the encoding phase.

//Next up, let's create the actual encoding function.

//The actual encoding logic is relatively straightforward for the most part. You simply take each of the letters in a given message and find its replacement character in the new alphabet.
function encode(message){
    let result = "";
    message = message.toLowerCase();
    for (let i = 0; i < message.length; i++){
        let index = alphabet.indexOf(message[i]);
        result += newalpha[index];
    }
    return result;
}

//Here you can see it in action with a n = 1 shift to the right.
//Decode
//Now that we have an encoded string, let's work our backwards to decode the new message.

//The process is essentially identical to the encoding. The only difference being that the new alphabet will be used as the lookup table.
function decode(message){
    let result = "";
    message = message.toLowerCase();
    for (let i = 0; i < message.length; i++){
        let index = newalpha.indexOf(message[i]);
        result += alphabet[index];
    }
    return result;
}
//And that is a quick implementation of the Caesar Cipher. It's important to note that you probably should not use this to secure either your own or your clients personal data.

//For that, you might want to take a look at encryption instead, which is different from either hashing or substituting.
