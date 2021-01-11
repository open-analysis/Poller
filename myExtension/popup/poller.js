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

/*
	Creates a button using a specified ID, class, innerHTML, and background style.
*/
function createNameButton(numBtns, b_id, b_class, b_text, b_bg)
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
	for(i = 0; i < button_array.length; i++)
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
	if (data)
	{
		let text = new Array();
		
		text = data.split('\n');
		
		numPeople = parseInt(text[0]);
		
		text.shift();
		
		//outputElem.textContent = numPeople;
		
		createNameButton(numPeople, "personButton", "button", text, '#8fd8ff');
	}
	else
	{
		console.log("Failed to get data");
	}
}

// changes the current list of buttons to a new
// set of buttons that are different
function button_clicked(name)
{	
	// clear the old set of buttons
	for (i= 0; i < numPeople; i++)
	{
		let tmpBtn = document.getElementById('personButton');
		divID.removeChild(tmpBtn);
	}
	
	// change the heading
	let heading = document.getElementById('heading');
	heading.innerHTML = name;

	/*
		This section creates a button with links to the article that's attached to the title.
		The for loop is for the number of news sites/text files that are in each person's folder
		Each section should say the news site's name
		The number of buttons created should be the same as the number of links provided
	*/
	/*
	for(i = 0; i < 3; i++)
	{
		var section = document.createElement('p');
		section.id = "newsSiteDiv";
		section.textContent = name;
		divID.appendChild(section);
		
		
		
		createNameButton(8, "linkButton", "button", "New Button!", '#ffffffff');
	}
	*/
	// temp solution to the above problem since there's only one file to deal with
	var section = document.createElement('p');
	section.id = "newsSiteDiv";
	section.textContent = "CNN";
	divID.appendChild(section);

	readNewsSite(name);
}

function readNewsSite(name)
{
	//const path = "http://localhost:3888/D:/Dev/Python/poli/Poller/ppl" + name + "/CNN_List.txt";
	const path = "../ppl/" + name + "/CNN_List.txt";
	
	fetch(path).then(function(response)
	{
		return response.text()
	}).then(function(text)
	{
		addNewsSiteButton(text);
	}).catch(function(err)
	{
		console.log('Fetch problem: ' + err.message);
	});
}

function addNewsSiteButton(data)
{		

	var outputElem = document.createElement('p');
	outputElem.id = "output";
	outputElem.textContent = "Output";
	divID.appendChild(outputElem);
	
	var text = new Array();
	var links = new Array();
	
	if (data)
	{		
		var tmpArr = data.split('\n');
		
		var numLinks = (tmpArr.length - 1) / 2;
		
		for (i = 0; i < numLinks; i++)
		{
			text[i] = tmpArr[0];
			tmpArr.shift();
			links[i] = tmpArr[0];
			tmpArr.shift();
		}
		
		createSiteButton(numLinks, "linkButton", "button", text, links, '#ffffffff');
	}
	else
	{
		console.log("Failed to get data");
	}
}

/*
	Creates a button using a specified ID, class, innerHTML/textContent, an array of links, and background style.
	Creates an a element and appends the button to it as a child.
*/
function createSiteButton(numBtns, b_id, b_class, b_text, b_link, b_bg)
{
	var outputElem = document.getElementById('output');
	
	// check if the input text is an array
	if (Array.isArray(b_text))
	{
		//var tmpLink = null;
		// create the new set of buttons
		for (i= 0; i < numBtns; i++)
		{
			var a = document.createElement('a');
			var newButton = document.createElement('button');
			var tmpLink = b_link[i];
			newButton.id = b_id;
			newButton.class = b_class;
			newButton.innerHTML = b_text[i];
			newButton.style.background = b_bg;
			
			a.href = tmpLink;
			
			a.appendChild(newButton);
			divID.appendChild(a);
			
			button_array[i] = newButton;
		}
	}
}


init();
















