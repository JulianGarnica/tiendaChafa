<template>
  <MiddleBox class="shadowHover centerDiv">
    <v-form v-model="formValid" @submit.prevent>
      <v-container>
        <v-row>
          <v-col cols="12" md="12">
            <h1>{{ titulo }}</h1>
          </v-col>

          <v-col cols="12" md="12">
            <slot />
          </v-col>

          <v-col cols="12" md="4">
            <v-text-field
              :rules="rules"
              :counter="10"
              label="Nombre"
              v-model="formData.nombre"
              required
            ></v-text-field>
          </v-col>

          <v-col cols="12" md="4">
            <v-text-field
              :rules="rules"
              :counter="10"
              label="Apellido"
              v-model="formData.apellido"
              required
            ></v-text-field>
          </v-col>

          <v-col cols="12" md="4">
            <v-text-field
              :rules="rules"
              :counter="3"
              type="number"
              label="Edad"
              v-model="formData.edad"
              required
            ></v-text-field>
          </v-col>

          <v-col cols="12" md="4">
            <v-select
              :rules="rules"
              :items="itemsSexo"
              label="Sexo"
              v-model="formData.sexo"
              required
            ></v-select>
          </v-col>

          <v-col cols="12" md="4">
            <v-text-field
              :rules="rules"
              label="correo"
              v-model="formData.correo"
              required
            ></v-text-field>
          </v-col>

          <v-col cols="12" md="4">
            <v-text-field
              :rules="rules"
              :counter="10"
              label="Teléfono"
              v-model="formData.telefono"
              type="number"
              required
            ></v-text-field>
          </v-col>
          <v-col cols="12" md="12">
            <v-container fluid>
              <v-radio-group v-model="formData.sistemaSalud" :rules="rules">
                <template>
                  <div>Sistema de salud</div>
                </template>
                <v-radio value="Isapre">
                  <template v-slot:label>
                    <div>Isapre</div>
                  </template>
                </v-radio>
                <v-radio value="Fonasa">
                  <template v-slot:label>
                    <div>Fonasa</div>
                  </template>
                </v-radio>
                <v-radio value="Particular">
                  <template v-slot:label>
                    <div>Particular</div>
                  </template>
                </v-radio>
                <v-radio value="Fuerzas Armadas">
                  <template v-slot:label>
                    <div>Fuerzas Armadas</div>
                  </template>
                </v-radio>
              </v-radio-group>
            </v-container>
          </v-col>

          <v-col cols="12" md="12">
            <v-container fluid>
              <template>
                <div style="text-align: left">Es alérgico a</div>
              </template>
              <v-checkbox v-model="formData.medicamentos">
                <template v-slot:label>
                  <div>Medicamentos</div>
                </template>
              </v-checkbox>
              <v-checkbox v-model="formData.alimentos">
                <template v-slot:label>
                  <div>Alimentos</div>
                </template>
              </v-checkbox>
              <v-checkbox v-model="formData.pastillas">
                <template v-slot:label>
                  <div>Pastillas</div>
                </template>
              </v-checkbox>
              <v-checkbox v-model="formData.otros">
                <template v-slot:label>
                  <div>Otros</div>
                </template>
              </v-checkbox>
            </v-container>
          </v-col>

          <v-col cols="12" md="12">
            <v-container fluid>
              <v-radio-group
                row
                v-model="formData.grupoSanguineo"
                :rules="rules"
              >
                <template v-slot:label>
                  <div>Grupo sanguíneo</div>
                </template>
                <v-radio value="A+">
                  <template v-slot:label>
                    <div>A+</div>
                  </template>
                </v-radio>
                <v-radio value="A-">
                  <template v-slot:label>
                    <div>A-</div>
                  </template>
                </v-radio>
                <v-radio value="B+">
                  <template v-slot:label>
                    <div>B+</div>
                  </template>
                </v-radio>
                <v-radio value="B-">
                  <template v-slot:label>
                    <div>B-</div>
                  </template>
                </v-radio>
                <v-radio value="AB+">
                  <template v-slot:label>
                    <div>AB+</div>
                  </template>
                </v-radio>
                <v-radio value="AB-">
                  <template v-slot:label>
                    <div>AB-</div>
                  </template>
                </v-radio>
              </v-radio-group>
            </v-container>
          </v-col>

          <v-col cols="12" md="12">
            <v-textarea
              name="input-7-1"
              v-model="formData.observaciones"
              label="Observaciones"
            ></v-textarea>
          </v-col>
          <v-col cols="12" md="12">
            <v-checkbox :rules="rules">
              <template v-slot:label>
                <div>Aceptar los términos y condiciones</div>
              </template>
            </v-checkbox>
          </v-col>

          <v-col cols="12" md="12">
            <v-btn
              color="success"
              class="mr-4"
              type="submit"
              :disabled="!formValid"
              @click="enviarDataChildren()"
            >
              Registrar
            </v-btn>

            <v-btn color="error" class="mr-4" @click="reset()" v-if="limpiar">
              Limpiar
            </v-btn>
          </v-col>
        </v-row>
      </v-container>
    </v-form>
  </MiddleBox>
</template>

<script>
import MiddleBox from "../components/static/MiddleBox.vue";

export default {
  name: "HomeView",
  components: {
    MiddleBox,
  },
  props: {
    formData: Object,
    titulo: String,
    limpiar: Boolean,
  },
  data: () => ({
    itemsSexo: [
      "Masculino",
      "Femenino",
      "Transformer",
      "No sé",
      "Venezolano",
      "Otro",
    ],
    formDataDefault: {
      nombre: "",
      apellido: "",
      edad: "",
      sexo: "",
      correo: "",
      telefono: "",
      sistemaSalud: "",
      medicamentos: false,
      alimentos: false,
      pastillas: false,
      otros: false,
      grupoSanguineo: "",
      observaciones: "",
    },
    formValid: false,
    rules: [
      (value) => {
        if (value) return true;

        return "Este campo es obligatorio";
      },
    ],
  }),
  methods: {
    enviarDataChildren: function () {
      this.$emit("enviarData");
    },
    reset: function () {
      this.formData = this.formDataDefault
    },
  },
};
</script>

<style scoped>
.home {
  background: #fff;
}

.centerDiv {
  margin-top: 50px !important;
}
</style>
