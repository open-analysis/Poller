var button_array = [];
var divID = document.getElementById('popup-content');
var i, numPeople;
numPeople = 4;

// init the popup with a number of buttons determined by 
// numPeople that  when clicked change to a different list of buttons
function init()
{
	
	read();
	
	createButton(numPeople, "personButton", "button", "Person's Name", '#8fd8ff');
	
	// adding the event listener to each of these buttons
	for(i = 0; i < numPeople; i++)
	{
		button_array[i].addEventListener("click", function() {
			personButton.style.background = '#689fbd';
			personButton.innerHTML = "Ayyyyy";
			button_clicked();
		});
	}
		
	
	//createButton(1, "personButton", "button", tmp[0][0], '#8fd8ff');
	
}

// changes the current list of buttons to a new
// set of buttons that are different
function button_clicked()
{
	// clear the old set of buttons
	for (i= 0; i < numPeople; i++)
	{
		var tmpBtn = document.getElementById('personButton');
		divID.removeChild(tmpBtn);
	}
	
	// change the heading
	var heading = document.getElementById('heading');
	heading.innerHTML = "New List!";
	
	createButton(numPeople*2, "newButton", "button", "New Button!", '#ffffffff');
	
}

/*
	Creates a button using a specified ID, class, innerHTML, and background style.
	Foregoes the creation of an event listener, meaning that it will have to be created 
	outside of this function by going through button_array.
*/
function createButton(numBtns, b_id, b_class, b_text, b_bg)
{
	// create the new set of buttons
	for (i= 0; i < numBtns; i++)
	{
		var newButton = document.createElement('button');
		newButton.id = b_id;
		newButton.class = b_class;
		newButton.innerHTML = b_text;
		newButton.style.background = b_bg;
		
		button_array[i] = newButton;
	}	
	
	// add the new buttons the screen
	for (i= 0; i < numBtns; i++)
	{
		divID.appendChild(button_array[i]);
	}
}

function read()
{
	const path = "D:/Dev/Python/poli/Poller/folders.txt";
	
	var output = document.createElement('p');
	output.id = "output";
	output.textContent = "I'm the output!";
	divID.appendChild(output);
	
	// need to find a way to read a locla file

}

init();















