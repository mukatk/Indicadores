var form = new Vue({
    el: '.div-indicadores',
    data: {
        indicadores: []
    },
    computed: {
        total: function () {
            var somatorio = 0;
            for (var i = 0; i < indicadores.length; i++) {
                somatorio += parseFloat(parseInt(indicadores[i].Porcentagem) * parseFloat(indicadores[i].Peso));
            }
            return somatorio;
        }
    },
    mounted: function () {
        this.buscaIndicadores();
        setInterval(this.buscaIndicadores, 180000);
    },
    methods: {
        buscaIndicadores: function () {
            const _self = this;

            _self.$http.get('/BuscaIndicadores').then(response => {
                var data = response.body.result;
                _self.indicadores = [];
                var somatoria = 0;
                for (var i = 0; i < data.length; i++) {
                    _self.indicadores.push(data[i]);
                }
            });
        },
        classeProgresso: function(porcentagem) {
            if (porcentagem < 50) 
                return 'red';
            else if (porcentagem < 80)
                return 'yellow';
            
            return 'green';
        },
        classeProgressoGeral: function() {
            if (this.total < 50) 
                return 'red';
            else if (this.total < 88)
                return 'yellow';
            
            return 'green';
        }
    }
});