/** @odoo-module */

import { WebClient } from "@web/webclient/webclient";
import { patch } from "@web/core/utils/patch";

patch(WebClient.prototype, "title_and_icon.WebClient", {
    setup() {
        this._super();
        var currentCompanyName  = this.env.services.company.currentCompany.name;
        this.title.setParts({ zopenerp:  currentCompanyName });
    },
});