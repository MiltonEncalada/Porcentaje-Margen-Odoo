odoo.define('product_margin.percentage_widget', function (require) {
    "use strict";

    var field_registry = require('web.field_registry');
    var FieldFloat = require('web.basic_fields').FieldFloat;

    var FieldPercentage = FieldFloat.extend({
        _renderReadonly: function () {
            this._super();
            this.$el.text(this.value.toFixed(this.digits[1]) + '%');
        },
        _renderEdit: function () {
            this._super();
            this.$input.val(this.value.toFixed(this.digits[1]));
            this.$input.after('<span>%</span>');
        }
    });

    field_registry.add('percentage', FieldPercentage);
});
