function copyPassword(){
	// get the password from the id 'password'
	var password = document.getElementById("passwords");
	console.log(password);

	//select the text
	password.select;
	password.setSelectionRange(0 , 9999); //for mobile

	//copy the selected password
	document.execCommand("copy");

	alert("Copied : " + password.value)
}