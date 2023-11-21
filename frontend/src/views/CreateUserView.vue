<template>
  <div>
    <formUser
      @enviarData="enviarData"
      :formData="formData"
      titulo="Crear Usuario"
      :limpiar="true"
    >
      <router-link :to="'/usuarios'">
        <v-btn class="mx-2" fab dark large color="cyan">
          <v-icon dark> mdi-keyboard-return </v-icon>
        </v-btn>
      </router-link></formUser
    >
  </div>
</template>

<script>
import MiddleBox from "../components/static/MiddleBox.vue";
import formUser from "@/components/formUser.vue";
import { insertUser } from "../api";

export default {
  name: "HomeView",
  components: {
    MiddleBox,
    formUser,
  },
  data: () => ({
    formData: {
      nombre: "",
      correo: "",
      password: "",
    },
  }),
  methods: {
    enviarData: function () {
      console.log(this.formData);
      insertUser(this.formData).then((response) => {
        console.log(response.data);
      });
    },
    reset: function () {
      console.log("Limpiando");
    },
  },
};
</script>

<style scoped>
.home {
  background: #fff;
}

.centerDiv {
  margin: 0 auto;
}
</style>
