var updateBtns = document.getElementsByClassName('saved-update')


for(var i = 0; i < updateBtns.length; i++){
    updateBtns[i].addEventListener('click', function(){
        var jobId = this.dataset.job
        var action = this.dataset.action
        console.log('jobId:', jobId, 'action:', action)

       
        updateSaved(jobId, action)
    })
}

function updateSaved(jobId, action){
    console.log('User is logged in, sending data..')

    var url = '/saved-job/'

    fetch(url, {
        method: 'POST',
        headers:{
            'Content-Type':'application/json',
            'X-CSRFToken': csrftoken,
        },
        body:JSON.stringify({'jobId':jobId, 'action':action})
    })

    .then((response) =>{
        return response.json()
    })

    .then((data) =>{
       console.log('data:', data)
       location.reload()
    })

}