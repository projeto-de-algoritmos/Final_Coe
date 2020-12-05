<template>
    <v-container class="d-flex flex-column align-center justify-center mb-4">
        <v-text-field
            
            class="text-center"
            v-model="peso"
            label="Qual a importância desse caminhão ?<br>
            1 - leve; 2 - leviana; 3 - média; 4 - muita; 5 - urgente" />

        <v-text-field
            class="text"
            v-model="horaChegada"
            label="Qual o horário de chegada do caminhão ?" />
        
        <v-text-field
            class="text"
            v-model="horaSaida"
            label="Qual o horário de saida do caminhão ?" />
        
    </v-container>
</template>

<script>
export default {
    data: () => ({
        peso: "",
        horaChegada: "",
        horaSaida: ""
    }),
    computed: {
        maiorSubSequencia() {
            return this.calculaMaiorSubsequencia(this.sequencia).max
        },
    },
    methods: {
        ordenaPorTempoTermino(){
            return 0
        },
        computaPesos(){
            return 0
        },
        encontraSolucao(){
            return 0
        },
    },
}
</script>

<style lang="scss">
.v-input {
    width: 100%;

    input {
        text-align: center;
    }
}
</style>