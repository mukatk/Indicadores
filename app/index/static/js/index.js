var form = new Vue({
    el: '.div-indicadores',
    data: {
        indicadores: []
    },
    computed: {
        total: function () {
            const _self = this;
            var somatorio = 0;
            for (var i = 0; i < _self.indicadores.length; i++) {
                somatorio += parseFloat(parseInt(_self.indicadores[i].Porcentagem) * parseFloat(_self.indicadores[i].Peso));
            }
            return somatorio;
        }
    },
    mounted: function () {
        const _self = this;
        _self.buscaIndicadores();
        setInterval(_self.buscaIndicadores, 180000);
    },
    methods: {
        atualizaIndicador: function (id, porcentagem) {
            const _self = this;

            _self.$http.post('/AtualizaIndicador', {
                Id: id,
                Porcentagem: porcentagem
            }).then(response => {
                Materialize.toast(response.body, 4000);
            });
        },
        buscaIndicadores: function () {
            const _self = this;

            _self.$http.get('/BuscaIndicadores').then(response => {
                var data = response.body.result;
                _self.indicadores = [];
                for (var i = 0; i < data.length; i++) {
                    _self.indicadores.push(data[i]);
                }
                Materialize.toast('Atualização concluída', 4000);
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