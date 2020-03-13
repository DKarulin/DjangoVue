<template>
    <div class="container">
<!--      <b-modal ref="my-modal" hide-footer>-->
<!--            <div class="d-block text-center mb-4">-->
<!--              <h3>Выберите дату!</h3>-->
<!--            </div>-->
<!--            <b-button class="mt-3" variant="outline-danger" block @click="hideModal">Закрыть</b-button>-->
<!--      </b-modal>-->
      <div class="row mb-5">
            <div class="col-md-8 col-12">
               <b-calendar
                 block
                 local="ru"
                 selected-variant="info"
                 :start-weekday= 1
                 @context="onContext"
                 v-model="value"
               ></b-calendar>
                  <div class="row mt-2 mb-2">
                    <div class="col-md-12 col-12">
                          <button type="button" class="btn btn-outline-primary" @click="addListDays(context)">Добавить</button>
                    </div>
                      <div class="col-md-12 col-12">
                        <button type="button" class="btn btn-outline-success mt-2">Отправить</button>
                      </div>
                    <div class="col-md-12 col-12">
                        <label>Рабочие дни:</label>
                        <div class="row mb-2 py-2 align-items-center" v-for="day in listDays" :key="day.selectedYMD">
                        <div class="col-md-10 col-10">
                              {{day.selectedFormatted}}
                        </div>
                        <div class="col-md-2 col-2">
                              <button type="button" class="btn btn-outline-danger btn-sm" @click="removeDayInList(day.selectedFormatted)">X</button>
                         </div>
                        </div>
                    </div>
                  </div>
            </div>
            <div class="col-md-4 col-12">
                   <div class="row mb-2 py-2 align-items-center border rounded" v-for="stuff in staffs" :key="stuff.Name">
                     <div class="col-md-6 col-5">
                       {{stuff.Name}}
                     </div>
                     <div class="col-md-6 col-5">
                       {{stuff.Surname}}
                     </div>
                   </div>
            </div>
    </div>
   {{context}}
   <hr class="mt-5">
   {{listDays}}
   <hr class="mt-5">
 </div>
</template>

<script>
export default {
  name: 'Manager',
  data() {
    return {
      value: '',
      context: null,
      listDays: [],
      flag: true,
      staffs: [
        {
          Name: 'Sasha',
          Surname: 'Petrov',
        },
        {
          Name: 'Danila',
          Surname: 'Karulin',
        },
        {
          Name: 'Vasya',
          Surname: 'Smirnov',
        },
        {
          Name: 'Max',
          Surname: 'Petrov',
        },
      ],
    };
  },
  methods: {
    onContext(ctx) {
      this.context = ctx;
    },

    addListDays(ctx) {
      // this.showModal();
      this.checkList();
      if (this.flag === true) {
        this.listDays.push(ctx);
      } else if (this.flag === false) {
        this.flag = true;
      }
    },
    checkList() {
      this.listDays.forEach((item) => {
        if (item.selectedFormatted === this.context.selectedFormatted) {
          this.flag = false;
        }
      });
    },
    removeDayInList(elem) {
      this.listDays.forEach((item) => {
        if (item.selectedFormatted === elem) {
          const index = this.listDays.indexOf(item);
          if (index > -1) {
            this.listDays.splice(index, 1);
          }
        }
      });
    },
  },
};
</script>

<style scoped>

</style>
