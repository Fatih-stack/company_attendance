$(document).ready(function() {
    $('#employeeTable').DataTable({
        "processing": true,
        "serverSide": true,
        "ajax": "/api/employees/",
        "columns": [
            { "data": "name" },
            { "data": "check_in_time" },
            { "data": "check_out_time" },
            { "data": "status" }
        ]
    });
});