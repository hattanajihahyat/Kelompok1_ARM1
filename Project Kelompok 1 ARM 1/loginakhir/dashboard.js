$(document).ready(function () {
  selesai();
});

var myArraymotor = [];
var myArrayhvac = [];
var myArraypompa = [];

function selesai() {
  setTimeout(function () {
    update();
    buildTablemotor(myArraymotor);
    buildTablehvac(myArrayhvac);
    buildTablepompa(myArraypompa);
    selesai();
  }, 3000);
}

//fungcion update
function update() {
  $.ajax({
    url: '/jsmotor',
    data: 'rvmotor',
    dataType: 'JSON',
    type: 'GET',
    success: function (data) {
      myArraymotor = data.rvmotor;
      console.log(data);

      $('#result').html();
      $('#result').append(data.htmlresponse);
    },
  });

  $.ajax({
    url: '/jshvac',
    data: 'rvhvac',
    dataType: 'JSON',
    type: 'GET',
    success: function (data) {
      myArrayhvac = data.rvhvac;
      console.log(data);

      $('#result').html();
      $('#result').append(data.htmlresponse);
    },
  });

  $.ajax({
    url: '/jspompa',
    data: 'rvpompa',
    dataType: 'JSON',
    type: 'GET',
    success: function (data) {
      myArraypompa = data.rvpompa;
      console.log(data);

      $('#result').html();
      $('#result').append(data.htmlresponse);
    },
  });
}

//motor----
function buildTablemotor(data) {
  var table = document.getElementById('mymotor');
  $('#mymotor').empty();

  for (var i = 0; i < data.length; i++) {
    var event_data = '';

    event_data += '<tr>';
    event_data += '<td>' + (i + 1) + '</td>';
    event_data += '<td>' + data[i].datetime + '</td>';
    event_data += '<td>' + data[i].status + '</td>';
    event_data += '<td>' + data[i].temperature + '</td>';
    event_data += '</tr>';

    $('#mymotor').append(event_data);
    $('#tempmotor').html(data[i].temperature);
  }
}

//hvac-----
function buildTablehvac(data) {
  var table = document.getElementById('myhvac');
  $('#myhvac').empty();

  for (var i = 0; i < data.length; i++) {
    var event_data = '';

    event_data += '<tr>';
    event_data += '<td>' + (i + 1) + '</td>';
    event_data += '<td>' + data[i].datetime + '</td>';
    event_data += '<td>' + data[i].status + '</td>';
    event_data += '<td>' + data[i].temperature + '</td>';
    event_data += '</tr>';

    $('#myhvac').append(event_data);
  }
}

//pompa------
function buildTablepompa(data) {
  var table = document.getElementById('mypompa');
  $('#mypompa').empty();

  for (var i = 0; i < data.length; i++) {
    var event_data = '';

    event_data += '<tr>';
    event_data += '<td>' + (i + 1) + '</td>';
    event_data += '<td>' + data[i].datetime + '</td>';
    event_data += '<td>' + data[i].status + '</td>';
    event_data += '<td>' + data[i].temperature + '</td>';
    event_data += '</tr>';

    $('#mypompa').append(event_data);
  }
}
