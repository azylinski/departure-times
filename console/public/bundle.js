var config = {};

base_url = 'http://192.168.99.100'

config.stop_finder_api = base_url + '/api/v1/stop_finder/'
config.core_api = base_url + '/api/v1/core/'


var messageBar = document.getElementById("message-bar"),
	departuresView = document.getElementById("departures-view");

// try geolocation
navigator.geolocation.getCurrentPosition(fetchDataForGivenLocation);

function fetchDataForGivenLocation(position) {
	var lat = position.coords.latitude,
		lng = position.coords.longitude;

    messageBar.innerHTML = "Latitude: " + lat + ", Longitude: " + lng;

    url = config.stop_finder_api + 'stops/?lat='+ lat +'&lng=' + lng;

    console.log(url);

    $.get(url, function(stop) {
    	console.log(stop);
    	messageBar.innerHTML = 'Nearest stop: ' + stop['title'];

    	url = config.core_api + 'departures/' + stop['tag']

	    $.get(url, function(data) {
	    	console.log(data['departures']);

			if (data['departures'].length == 0) {
				var tableHtml = '<p>No data for given stop.<br/>Sorry =(</p>';
			} else {
		    	var tableHtml = '<table class="mdl-data-table mdl-js-data-table" style="width: 100%"><thead><tr>'
		    		+ '<th class="mdl-data-table__cell--non-numeric">Time</th>'
		    		+ '<th class="mdl-data-table__cell--non-numeric">Route</th>'
		    		+ '<th class="mdl-data-table__cell--non-numeric">Destination</th>'
		    		+ '</tr></thead><tbody>';

		    	data['departures'].forEach(function(row) {
		    		tableHtml += '<tr>'
						+ '<td class="mdl-data-table__cell--non-numeric">'+ row['departure_at'] +'</td>'
					    + '<td class="mdl-data-table__cell--non-numeric">'+ row['route'] +'</td>'
					    + '<td class="mdl-data-table__cell--non-numeric">'+ row['destination'] +'</td>'
				    + '</tr>';
				});
		    	tableHtml += '</tbody></table>';
			}

	    	departuresView.innerHTML = tableHtml;
    	});
	});
}
