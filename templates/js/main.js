'use strict';

var rowCount = $('table tbody tr').length,
	rowHelper;

$(document).on('click', '.edit', function() {
    $(this).parent().siblings('td.data').each(function() {
        var content = $(this).html();
        $(this).html('<input value="' + content + '" />');
    });

    $(this).siblings('.save').show();
    $(this).siblings('.delete').hide();
    $(this).hide();
});

$(document).on('click', '.save', function() {
    $(this).parents('tr').find('input').each(function() {
        if (!$(this).val()) {
        	var content = ' ';
        } else {
            var content = $(this).val();
        }

        $(this).html(content);
        $(this).contents().unwrap();
    });
    $(this).siblings('.edit').show();
    $(this).siblings('.delete').show();
    $(this).hide();
});


$(document).on('click', '.delete', function() {
    rowCount -= 1;
    rowHelper = 0;
    $(this).parents('tr').remove();

    $('.rowNum').each(function() {
	    	rowHelper += 1;
        $(this).text(rowHelper);
    });
});

$('.add').click(function() {
    rowCount += 1;
    $(this).parents('table').append('<tr><th scope="row" class="rowNum">' + rowCount + '</th><td class="data"></td><td class="data"></td><td class="data"></td><td class="data"></td><td class="data"></td><td class="operations-wr"><button class="btn btn-success save">Save</button><button class="btn btn-warning edit">Edit</button><button class="btn btn-danger delete">Delete</button></td></tr>');
});