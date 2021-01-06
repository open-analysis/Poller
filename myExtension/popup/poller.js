var button_array = [];
var divID = document.getElementById('popup-content');
var i, numPeople;
numPeople = 2;

// init the popup with a number of buttons determined by 
// numPeople that  when clicked change to a different list of buttons
function init()
{			
	readNames();
	
}

// changes the current list of buttons to a new
// set of buttons that are different
function button_clicked(name)
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

	/*
		This section creates a button with links to the article that's attached to the title.
		The for loop is for the number of news sites/text files that are in each person's folder
		Each section should say the news site's name
		The number of buttons created should be the same as the number of links provided
	*/
	for(i = 0; i < 3; i++)
	{
		var section = document.createElement('p');
		section.id = "newsSiteDiv";
		section.textContent = name;
		divID.appendChild(section);
		
		createButton(8, "linkButton", "button", "New Button!", '#ffffffff');
	}
	
}

/*
	Creates a button using a specified ID, class, innerHTML, and background style.
	Foregoes the creation of an event listener, meaning that it will have to be created 
	outside of this function by going through button_array.
*/
function createButton(numBtns, b_id, b_class, b_text, b_bg)
{
	// check if the input text is an array
	if (Array.isArray(b_text))
	{
		// create the new set of buttons
		for (i= 0; i < numBtns; i++)
		{
			var newButton = document.createElement('button');
			newButton.id = b_id;
			newButton.class = b_class;
			newButton.innerHTML = b_text[i];
			newButton.style.background = b_bg;
			
			button_array[i] = newButton;
		}	
		
		// add the new buttons the screen
		for (i= 0; i < numBtns; i++)
		{
			divID.appendChild(button_array[i]);
		}
	}
	else 
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
	
	// adding the event listener to each of these buttons
	for(i = 0; i < numBtns; i++)
	{
		button_array[i].addEventListener("click", function() {
			//this.style.background = '#689fbd';
			button_clicked(this.textContent);
		})
	}
	
}

function readNames()
{
	const path = "../folders.txt";
	
	/*
	var output = document.createElement('p');
	output.id = "output";
	output.textContent = "I'm the output!";
	divID.appendChild(output);
	*/
	
	fetch(path).then(function(response)
	{
		return response.text()
	}).then(function(text)
	{
		//return text;
		addNameToButton(text);
	}).catch(function(err)
	{
		console.log('Fetch problem: ' + err.message);
	});
}

function addNameToButton(data)
{
	//var outputElem = document.getElementById('output');
	
	if (data)
	{
		let text = new Array();
		
		text = data.split('\n');
		
		numPeople = parseInt(text[0]);
		
		text.shift();
		
		//outputElem.textContent = numPeople;
		
		createButton(numPeople, "personButton", "button", text, '#8fd8ff');
	}
	else
	{
		outputElem.textContent = "Failed to get data";
	}
}

function readNewsSite(name)
{
	const path = "../ppl.txt" + name + "/cnn.txt";
	
	var output = document.createElement('p');
	output.id = "output";
	output.textContent = "I'm the output!";
	divID.appendChild(output);
	
	fetch(path).then(function(response)
	{
		return response.text()
	}).then(function(text)
	{
		//return text;
		output.textContent = text;
	}).catch(function(err)
	{
		console.log('Fetch problem: ' + err.message);
	});
}

init();















