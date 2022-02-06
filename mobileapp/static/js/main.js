function resellershow(){
    usertype=document.getElementById('usertype');
    reseller=document.getElementById('reseller');
    customer=document.getElementById('custom');
    bankdetails=document.getElementById('bankdetails');
    if(usertype.value=="reseller"){
        reseller.style.display='block';
        bankdetails.style.display='block';
        customer.style.display="none";
    }
    else{
        reseller.style.display='none';
        bankdetails.style.display='none';
        customer.style.display="block";

    }

}

function validatesignup(){
    
    usertype=document.getElementById('usertype')
    
    fname=document.getElementById('firstname')
    mobile=document.getElementById('mobile')
    console.log(mobile.value)
    gender=document.getElementById('gender')
    dob=document.getElementById('dob')
    address=document.getElementById('address')
    country=document.getElementById('country')
    companyname=document.getElementById('companyname')
    companyid=document.getElementById('companyid')
    accountholder=document.getElementById('accnthldr')
    accountnumber=document.getElementById('accntno')
    accountifsc=document.getElementById('ifsccode')
    setstatus=1
    if(usertype.value =='reseller'){

    }
    else{
        if(fname.value==""){
            
            fname.style.borderColor="red";
            setstatus=0

        }
        var phonereg= /^[6-9]{1}[0-9]{9}$/;
        if(mobile.value==""){
            console.log("hai")
            mobile.style.borderColor="red";
            setstatus=0
        }

       if(mobile.value.match(phonereg)){
            mobile.style.borderColor="green";
            setstatus=1
        }
        else{
            console.log("error")
            mobile.style.borderColor="red";
            setstatus=0

            }

        var emailreg=/^([a-zA-Z0-9_\.\-])+\@(([a-zA-Z0-9\-])+\.)+([a-zA-Z0-9]{2,4})+$/;
        if(email.value.match(emailreg)){
            email.style.borderColor="green";
            setstatus=1
        }
        else{
            console.log("error")
            email.style.borderColor="red";
            setstatus=0

            }

    }

    if(setstatus=0){
        return false
    }

}
