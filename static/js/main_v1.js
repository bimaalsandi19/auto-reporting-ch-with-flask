$(document).ready(function() {
    $.datepicker.setDefaults({
        dateFormat : 'yy-mm-dd'
    });
    $(function(){
        $("#from_date").datepicker();
        $("#to_date").datepicker();
    });

    $("#filter").click(function(){
        var action = 'fetch_data';
        var from_date = $('#from_date').val();
        var to_date = $('#to_date').val();
        var area = $('#area').val();
        var region = $('#region').val();

        $.ajax({
            url : 'fetch_data.php',
            type : 'POST',
            data : {action:action,from_date:from_date, to_date:to_date, area:area, region:region},
            beforeSend: function() {
                $('.result').html("<h4 class='text-center'>Working...</h4>")
            },
            success: function(data) {
                $('.result').html(data)
            }
        })

    //    if (from_date != '' && to_date != '' && area !='' && region !='' ) {
    //         $.ajax({
    //             url : 'filter_data.php',
    //             method : 'POST',
    //             data : {from_date:from_date, to_date:to_date, area:area, region:region},
    //             beforeSend: function() {
    //                 $('.result').html("<h4 class='text-center'>Working...</h4>")
    //             },
    //             success: function(data) {
    //                 $('.result').html(data)
    //             }
    //         });
    //     }
        
        
    });

    // $('#area').on('change', function() {
    //     var value = $(this).val();
    //     // alert(value);
    //     $.ajax({
    //         url: 'filter.php',
    //         type: 'POST',
    //         data: 'area=' + value,
    //         beforeSend: function() {
    //             $('.result').html("<h4 class='text-center'>Working...</h4>")
    //         },
    //         success: function(data) {
    //             $('.result').html(data)
    //         }
    //     })
    // })


    // $('#region').on('change', function() {
    //     var value = $(this).val();
    //     // alert(value);

    //     $.ajax({
    //         url: 'filter.php',
    //         type: 'POST',
    //         data: 'region=' + value,
    //         beforeSend: function() {
    //             $('.result').html("<h4 class='text-center'>Working...</h4>")
    //         },
    //         success: function(data) {
    //             $('.result').html(data)
    //         }
    //     })
    // })
 

    $("#area").change(function() {
        var area = $("#area").val();
        $.ajax({
            type: 'POST',
            dataType: 'html',
            url: 'getregion',
            data: 'area=' + area,
            success: function(data) {
                $('#region').html(data)
            }
        })
    })
});

function trendTicketAndSLA() {
        
    // Choose the element id which you want to export.
    var element = document.getElementById('myChart01');
    element.style.width = '992px';
    element.style.height = 'auto';
    var opt = {
        margin:      0,
        filename:     'Trend Ticket And SLA.pdf',
        image:        { type: 'jpeg', quality: 1 },
        html2canvas:  { scale: 1 },
        jsPDF:        { unit: 'in', format: 'letter', orientation: 'landscape',precision: '12' }
      };
    
    html2pdf().set(opt).from(element).save();
  }

function trendTicketAndSLARegion() {
        
    // Choose the element id which you want to export.
    var element = document.getElementById('myChart02');
    element.style.width = '992px';
    element.style.height = 'auto';
    var opt = {
        margin:       0,
        filename:     'Trend Ticket And SLA Region.pdf',
        image:        { type: 'jpeg', quality: 1 },
        html2canvas:  { scale: 1 },
        jsPDF:        { unit: 'in', format: 'letter', orientation: 'landscape',precision: '12' }
      };
    
    html2pdf().set(opt).from(element).save();
  }

function recon() {
        
    // Choose the element id which you want to export.
    var element = document.getElementById('tableRecon');
    element.style.width = 'auto';
    element.style.height = 'auto';
    var opt = {
        margin:       0,
        filename:     'Recon.pdf',
        image:        { type: 'jpeg', quality: 2 },
        html2canvas:  { scale: 2 },
        jsPDF:        { unit: 'in', format: 'letter', orientation: 'landscape' ,precision: '12' }
      };
    
    html2pdf().set(opt).from(element).save();
  }

function olaCem() {
        
    // Choose the element id which you want to export.
    var element = document.getElementById('myChart03');
    element.style.width = 'auto';
    element.style.height = 'auto';
    var opt = {
        margin:       1,
        filename:     'OLA CEM.pdf',
        image:        { type: 'jpeg', quality: 2 },
        html2canvas:  { scale: 1 },
        jsPDF:        { unit: 'in', format: 'letter', orientation: 'landscape' ,precision: '12' }
      };
    
    html2pdf().set(opt).from(element).save();
  }

function olaResp() {
        
    // Choose the element id which you want to export.
    var element = document.getElementById('myChart04');
    element.style.width = 'auto';
    element.style.height = 'auto';
    var opt = {
        margin:       1,
        filename:     'OLA RESP.pdf',
        image:        { type: 'jpeg', quality: 2 },
        html2canvas:  { scale: 1 },
        jsPDF:        { unit: 'in', format: 'letter', orientation: 'landscape' ,precision: '12' }
      };
    
    html2pdf().set(opt).from(element).save();
  }

function olaNo() {
        
    // Choose the element id which you want to export.
    var element = document.getElementById('myChart05');
    element.style.width = 'auto';
    element.style.height = 'auto';
    var opt = {
        margin:       1,
        filename:     'OLA NO.pdf',
        image:        { type: 'jpeg', quality: 2 },
        html2canvas:  { scale: 1 },
        jsPDF:        { unit: 'in', format: 'letter', orientation: 'landscape' ,precision: '12' }
      };
    
    html2pdf().set(opt).from(element).save();
  }

  function olaCes() {
        
    // Choose the element id which you want to export.
    var element = document.getElementById('myChart05');
    element.style.width = 'auto';
    element.style.height = 'auto';
    var opt = {
        margin:       1,
        filename:     'OLA CES.pdf',
        image:        { type: 'jpeg', quality: 2 },
        html2canvas:  { scale: 1 },
        jsPDF:        { unit: 'in', format: 'letter', orientation: 'landscape' ,precision: '12' }
      };
    
    html2pdf().set(opt).from(element).save();
  }
  function result() {
        
    // Choose the element id which you want to export.
    var element = document.getElementById('result');
    element.style.width = 'auto';
    element.style.height = 'auto';
    var opt = {
        margin:       0,
        filename:     'B2B CH.pdf',
        image:        { type: 'jpeg', quality: 2 },
        html2canvas:  { scale: 0 },
        jsPDF:        { unit: 'in', format: 'letter', orientation: 'landscape' ,precision: '12' }
      };
    
    html2pdf().set(opt).from(element).save();
  }