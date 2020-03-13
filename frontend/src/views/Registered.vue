<template>
  <div class="container text-center">
    <div class="row">
      <div class="col-md-12 col-12 mt-5">
        <h3>Регистрация</h3>
      </div>
    </div>
    <div class="row">
      <div class="col-md-12 col-12">
        <img class="mb-4 rounded" src="../assets/picReg.png" alt="" width="72" height="72">
      </div>
    </div>
      <div class="row">
        <div class="col-md-12 col-12">
              <b-form @submit="onSubmit" @reset="onReset">
                <div class="col-md-4 offset-md-4">
                    <b-form-group id="input-group-2" label-for="input-2">
                      <b-form-input
                        id="input-2"
                        v-model="form.name"
                        required
                        placeholder="Введите имя"
                      ></b-form-input>
                    </b-form-group>
                </div>
                <div class="col-md-4 offset-md-4">
                    <b-form-group id="input-group-5" label-for="input-5">
                      <b-form-input
                        id="input-5"
                        v-model="form.surname"
                        required
                        placeholder="Введите фамилию"
                      ></b-form-input>
                    </b-form-group>
                </div>
                <div class="col-md-4 offset-md-4">
                    <b-form-group
                      id="input-group-1"
                      label-for="input-1"
                    >
                      <b-form-input
                        id="input-1"
                        v-model="form.email"
                        type="email"
                        required
                        placeholder="Введите почту"
                      ></b-form-input>
                    </b-form-group>
                </div>
                <div class="col-md-4 offset-md-4">
                    <b-form-group id="input-group-3" label-for="input-3">
                      <b-form-select
                        id="input-3"
                        v-model="form.position"
                        :options="position"
                        required
                      ></b-form-select>
                    </b-form-group>
                </div>
                <div class="col-md-4 offset-md-4">
                  <b-form-group id="input-group-6" label="Введите телефон" label-for="input-6">
                     <the-mask :mask="['+#(###)###-####']"
                               id="input-6"
                               class="rounded-sm"
                               v-model="form.telephone"
                               required/>
                  </b-form-group>
                </div>
                  <div class="col-md-4 offset-md-4">
                        <b-form-group label="Password" label-for="text-password" id="text-password" class="text-left">
                                <b-form-input type="password"
                                         id="text-password"
                                         aria-describedby="password-help-block"
                                         v-model="form.password"
                                         :state="validation"
                                         required></b-form-input>
                                <b-form-invalid-feedback :state="validation">
                                         Ваш пароль должен быть длиной не меньше 8 символов, но не более 20
                                </b-form-invalid-feedback>
                                <b-form-valid-feedback :state="validation">
                                          Отлично
                                </b-form-valid-feedback>
                        </b-form-group>
                  </div>
                  <div class="row text-left">
                       <div class="col-md-3 offset-md-4 col-12">
                         <b-button type="reset" variant="outline-danger" class="mr-3 mt-4">Очистить форму</b-button>
                       </div>
                       <div class="col-md-3 col-12">
                          <b-button type="submit" variant="outline-primary" class="mt-4" @click="fetchLogIn">Регистрация</b-button>
                       </div>
                 </div>

              </b-form>
              <b-card class="mt-3" header="Form Data Result">
                <pre class="m-0">{{ form }}</pre>
              </b-card>
        </div>
      </div>
  </div>
</template>

<script>
export default {
  name: 'Registered',
  data() {
    return {
      form: {
        name: '',
        surname: '',
        email: '',
        position: null,
        telephone: '',
        password: '',
      },
      position: [{ text: 'Выберите должность', value: null }, 'Руководитель', 'Работник'],
      show: true,
    };
  },
  computed: {
    validation() {
      return this.form.password.length >= 8 && this.form.password.length <= 20;
    },
  },
  methods: {
    onSubmit() {
      if (this.form.telephone.length === 11 && this.form.password.length >= 8 && this.form.password.length <= 20) {
        alert(JSON.stringify(this.form));
      }
    },
    onReset(evt) {
      evt.preventDefault();
      // Reset our form values
      this.form.email = '';
      this.form.name = '';
      this.form.surname = '';
      this.form.position = null;
      this.form.telephone = '';
      this.form.password = '';
      this.show = false;
      this.$nextTick(() => {
        this.show = true;
      });
    },
    async fetchLogIn() {
      const response = await fetch('http://127.0.0.1:8000/api/users/', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json;charset=utf-8',
        },
        body: JSON.stringify(this.form),
      });
      if (response.status === 201) {
        this.$router.push({ path: 'Manager' });
      }
    },
  },
};
</script>

<style scoped>

</style>
