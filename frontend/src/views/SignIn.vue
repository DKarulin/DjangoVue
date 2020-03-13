<template>
    <div class="container text-center mt-5">
      <img class="mb-4" src="../assets/picReg.png" alt="" width="72" height="72">
          <h1 class="h3 mb-3 font-weight-normal">Вход</h1>
             <label for="inputEmail" class="sr-only">Email address</label>
               <input type="email" id="inputEmail" class="form-control mb-4" placeholder="Email address" required autofocus>
                  <label for="inputPassword" class="sr-only">Password</label>
                     <input type="password" id="inputPassword" class="form-control mb-2" placeholder="Password" required>
                     <div class="checkbox mb-3">
                     <label>
                         <input type="checkbox" value="remember-me"> Запомнить пароль
                     </label>
                      </div>
                      <button class="btn btn-lg btn-primary btn-block" type="submit">Войти</button>
    </div>
</template>

<script>
export default {
  name: 'SignIn',
};
</script>

<style scoped>
</style>
