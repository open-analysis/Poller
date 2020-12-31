var button_array = [];
var divID = document.getElementById('popup-content');
var i, numPeople;
numPeople = 4;

// init the popup with a number of buttons determined by 
// numPeople that  when clicked change to a different list of buttons
function init()
{
	for (i= 0; i < numPeople; i++)
	{
		var personButton = document.createElement('button');
		personButton.id = "personButton";
		personButton.class = "button";
		personButton.innerHTML = "Person's Name";
		personButton.style.background = '#8fd8ff';
		
		personButton.addEventListener("click", function() {
			personButton.style.background = '#689fbd';
			personButton.innerHTML = "Ayyyyy";
			button_clicked();
		});
		
		button_array[i] = personButton;
	}
	
	for (i= 0; i < numPeople; i++)
	{
		divID.appendChild(button_array[i]);
	}
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
	
	// create the new set of buttons
	button_array = [];
	for (i= 0; i < numPeople*2; i++)
	{
		var newButton = document.createElement('button');
		newButton.id = "personButton";
		newButton.class = "button";
		newButton.innerHTML = "New Button!";
		newButton.style.background = '#ffffffff';
		
		newButton.addEventListener("click", function() {
			newButton.style.background = '#000000';
			newButton.innerHTML = "Ayyyyy again";
		});
		
		button_array[i] = newButton;
	}	
	
	// add the new buttons the screen
	for (i= 0; i < numPeople*2; i++)
	{
		divID.appendChild(button_array[i]);
	}
}

init();















