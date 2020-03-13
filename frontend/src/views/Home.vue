<template>
  <div>
    <button :disabled="!previousPage" @click="fetchCars(previousPage)">&lt;</button>
    <button class="btn btn-primary" :disabled="!nextPage" @click="fetchCars(nextPage)">&gt;</button>
    <table class="table">
      <thead class="thead-dark">
        <tr>
           <th>Vendor</th>
           <th>Model</th>
           <th>Year</th>
           <th>Volume</th>
           <th>Delete</th>
        </tr>
      </thead>
         <tbody>
           <tr v-for="car in cars" v-bind:key="car.id">
              <td>{{car.vendor}}</td>
              <td>{{car.model}}</td>
              <td>{{car.year}}</td>
              <td>{{car.volume}}</td>
              <td>
                <button type="button" class="btn btn-danger" @click="removeCar(car)">Delete</button>
              </td>
           </tr>
         </tbody>
    </table>
    <button @click="addFilter">+</button>
     <ul>
       <li v-for="filter in filters" v-bind:key="filter.id">
          <input v-model="filter.key">
          <input v-model="filter.value">
         <button @click="dropFilter(filter)">-</button>
       </li>
     </ul>

    <input placeholder="vendor" v-model="currentCar.vendor">
    <input placeholder="model" v-model="currentCar.model">
    <input placeholder="year" v-model.number="currentCar.year">
    <input placeholder="volume" v-model.number="currentCar.volume">
    <button type="button" class="btn btn-primary btn-sm" v-on:click="createCar">Create</button>
  </div>
</template>

<script>


export default {
  name: 'Home',
  data() {
    return {
      cars: [],
      currentCar: {},
      nextPage: null,
      previousPage: null,
      filters: [],
    };
  },
  async created() {
    this.fetchCars();
  },
  methods: {
    async fetchCars(url = 'http://127.0.0.1:8000/api/cars/') {
      const response = await fetch(url);
      const { results, next, previous } = await response.json();
      this.cars = results;
      this.nextPage = next;
      this.previousPage = previous;
    },
    async createCar() {
      const response = await fetch('http://127.0.0.1:8000/api/cars/', {
        method: 'POST',
        body: JSON.stringify(this.currentCar),
      });
      if (response.status !== 201) {
        alert(JSON.stringify(await response.json(), null, 2));
      }
      await this.fetchCars();
    },
    async removeCar(car) {
      const { id } = car;
      const response = await fetch(`http://127.0.0.1:8000/api/cars/${id}/`, {
        method: 'DELETE',
      });
      if (response.status !== 204) {
        alert(JSON.stringify(await response.json(), null, 2));
      }
      await this.fetchCars();
    },
    addFilter() {
      this.filters.push({ id: Math.random() });
    },
    dropFilter(filter) {
      this.filters = this.filters.filter((f) => f.id !== filter.id);
    },
  },
};
</script>
