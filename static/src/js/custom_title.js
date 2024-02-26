/** @odoo-module */

import { WebClient } from "@web/webclient/webclient";
import { patch } from "@web/core/utils/patch";

patch(WebClient.prototype, {
    setup() {
        super.setup();
        var currentCompanyName  = this.env.services.company.currentCompany.name;
        this.title.setParts({ zopenerp:  currentCompanyName });
    },
});