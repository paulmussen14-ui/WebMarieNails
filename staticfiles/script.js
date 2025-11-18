    document.addEventListener("DOMContentLoaded", () => {
    // PON AQUÍ TU NÚMERO, con código de país (Perú: 51)
    const WHATSAPP_NUMBER = "51954382592"; // <-- reemplaza X por tu número

    const forms = document.querySelectorAll(".service-form");

    function normalizar(texto) {
        return texto.normalize("NFD").replace(/[\u0300-\u036f]/g, "");
    }

    forms.forEach((form) => {
        form.addEventListener("submit", (e) => {
        e.preventDefault();

        const servicio = form.getAttribute("data-servicio") || "Servicio Marie Nails";
        const nombre = form.nombre.value.trim();
        const telefonoCliente = form.telefono.value.trim();
        const fecha = form.fecha.value;
        const hora = form.hora.value;
        const nota = form.nota.value.trim();

        if (!nombre || !telefonoCliente || !fecha || !hora) {
            alert("Por favor completa nombre, WhatsApp, fecha y hora.");
            return;
        }

        // Formatear fecha a dd/mm/aaaa
        let fechaFormateada = fecha;
        if (fecha.includes("-")) {
            const [yyyy, mm, dd] = fecha.split("-");
            fechaFormateada = `${dd}/${mm}/${yyyy}`;
        }

        let mensaje = `Hola, soy ${nombre}. Quisiera reservar una cita en Marie Nails.%0A%0A`;
        mensaje += `Servicio: ${servicio}%0A`;
        mensaje += `Fecha: ${fechaFormateada}%0A`;
        mensaje += `Hora: ${hora}%0A`;
        mensaje += `Mi WhatsApp: ${telefonoCliente}%0A`;
        if (nota) {
            mensaje += `%0ANota: ${nota}`;
        }

        const url = `https://wa.me/${WHATSAPP_NUMBER}?text=${mensaje}`;
        window.open(url, "_blank");
        });
    });
    });
