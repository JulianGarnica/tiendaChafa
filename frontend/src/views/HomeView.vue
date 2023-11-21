<template>
  <FullBoxVue class="shadowHover centerDiv">

    <h1>Registros de ficha médicas</h1>
    <router-link :to="'/crearFichaMedica'">
      <v-btn class="mx-2" fab dark large color="cyan">
        <v-icon dark> mdi-plus </v-icon>
      </v-btn>
    </router-link>

    <router-link :to="'/usuarios'">
      <v-btn class="mx-2" dark large color="cyan">
        Usuarios
      </v-btn>
    </router-link>
    <v-data-table
      :headers="headers"
      :items="dataResponse"
      :search="search"
      :items-per-page="30"
      class="elevation-1"
    >
      <template v-slot:item.actions="{ item }">
        <v-btn class="mx-2" fab dark small color="cyan" @click="editItem(item)"
          ><v-icon small> mdi-pencil </v-icon></v-btn
        >
        <v-btn
          class="mx-2"
          fab
          dark
          small
          color="error"
          @click="deleteItem(item)"
          ><v-icon small> mdi-delete </v-icon></v-btn
        >
      </template>
    </v-data-table>
    <v-dialog v-model="dialogDelete" max-width="500px">
      <v-card>
        <v-card-title class="text-h6" style="text-align: center"
          >¿Estás seguro/a de eliminar este item?</v-card-title
        >
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn color="blue darken-1" text @click="closeDelete">Cancel</v-btn>
          <v-btn color="blue darken-1" text @click="deleteItemConfirm"
            >OK</v-btn
          >
          <v-spacer></v-spacer>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </FullBoxVue>
</template>

<script>
import FullBoxVue from "../components/static/FullBox.vue";
import { getFichasMedicas, deleteFichaMedica } from "../api";

export default {
  name: "HomeView",
  components: {
    FullBoxVue,
  },
  data: () => ({
    headers: [
      { text: "Nombre", align: "start", value: "nombre" },
      { text: "Apellido", value: "apellido" },
      { text: "Correo", value: "correo" },
      { text: "Sexo", value: "sexo" },
      { text: "Acciones", value: "actions", sortable: false },
    ],
    dataResponse: [],
    search: "",
    idSelected: 0,
    dialogDelete: false,
  }),
  methods: {
    getData: function () {
      getFichasMedicas().then((response) => {
        this.dataResponse = response.data;
      });
    },
    editItem: function (item) {
      this.$router
        .push({ path: "/editarFichaMedica/" + item.id })
        .catch(() => {});
    },
    deleteItem: function (item) {
      this.idSelected = item.id;
      this.dialogDelete = true;
    },

    deleteItemConfirm: function () {
      deleteFichaMedica(this.idSelected).then((response) => {this.getData();});

      this.dialogDelete = false;

    },

    closeDelete: function () {
      this.dialogDelete = false;
    },
  },
  mounted() {
    this.getData();
  },
};
</script>

<style scoped>
.home {
  background: #fff;
}

.centerDiv {
  margin: 50px !important;
}
</style>
