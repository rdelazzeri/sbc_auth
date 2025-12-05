document.body.addEventListener('htmx:configRequest', (event) => {
    event.detail.headers['X-CSRFToken'] = '{{ csrf_token }}';
});

document.body.addEventListener('htmx:responseError', (event) => {
    console.log(event);
    alert(`Error: ${JSON.stringify(event.detail.xhr)}`);
    const {detail} = event;
    alert(`Error: ${detail.xhr.status}\nMessage: ${detail.xhr.statusText}`);
});



function toggle_selection(source) { 
    var btn = document.getElementsByName('btn-selection')[0];
    var checkboxes = document.getElementsByName('selection'); 
    var btn_value = ((btn.value=='true') ? true : false);
    for (let checkbox of checkboxes) {  
        checkbox.checked = btn_value;
    }; 
    if (btn_value){
        btn.value = 'false';
        btn.innerHTML = 'Deselect all'
    }
    else {
        btn.value = 'true';
        btn.innerHTML = 'Select all'
    }
} 



function bulk_modal(source, url) { 
    var checkboxes = document.getElementsByName('selection'); 
    var ids = [];
    for (let checkbox of checkboxes) {  
        if (checkbox.checked){
          ids.push(checkbox.value)
        }
    }; 
    console.log(ids.toString())
    htmx.ajax('GET', url, { 
      swap: 'innerHTML',
      target:"#base-modal",
      values: {'id': ids}
      }
    );
    var myModal = new bootstrap.Modal(document.getElementById('base-modal'),)
    myModal.toggle()
} 