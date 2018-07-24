var hideRegister = document.getElementById('register-form');

hideRegister.style.display = 'none';

var register = document.getElementById('register');
register.style.background = 'none';

function myFunction(){
    var hideLogin = document.getElementById('login-form');
    var hideRegister = document.getElementById('register-form');

    hideLogin.style.display = 'block';
    hideRegister.style.display = 'none';
}

function myRFunction(){
    var hideLogin = document.getElementById('login-form');
    var hideRegister = document.getElementById('register-form');

    hideLogin.style.display = 'none';
    hideRegister.style.display = 'block';
    
    

}

