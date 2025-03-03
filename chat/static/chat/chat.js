$(document).ready(function() {
    const userId = "{{ request.session.user_id }}";  // Obtém o ID do utilizador autenticado

    console.log("📡 Pusher iniciado para o utilizador ID:", userId);  // Verificar se está a iniciar corretamente

    // Configurar Pusher
    const pusher = new Pusher("9505bbfcec175b686952", {
        cluster: "eu",
        encrypted: true
    });

    // Inscrever-se no canal privado do utilizador autenticado
    const channelName = `private-chat-${userId}`;
    console.log(`🔗 A inscrever-se no canal: ${channelName}`);  // Debug

    const channel = pusher.subscribe(channelName);

    // Escutar eventos de novas mensagens
    channel.bind("new-message", function(data) {
        console.log("📩 Nova mensagem recebida:", data);  // Debug no console
        $("#chat-box").append(`<p><strong>${data.sender_nome} ${data.sender_apelido}:</strong> ${data.message}</p>`);
    });

    // Enviar mensagem via AJAX
    $("#chat-form").submit(function(event) {
        event.preventDefault();
        let receiverId = $("#receiver").val();  // Seleciona o destinatário
        let message = $("#message").val();

        console.log("✉️ A enviar mensagem:", message);  // Debug no console

        $.ajax({
            type: "POST",
            url: "/chat/send_message/",
            contentType: "application/json",
            data: JSON.stringify({
                receiver_id: receiverId,
                message: message
            }),
            headers: { "X-CSRFToken": "{{ csrf_token }}" },
            success: function(response) {
                console.log("✅ Mensagem enviada com sucesso para o backend");
                $("#message").val("");  // Limpa o campo após enviar
            },
            error: function(xhr, status, error) {
                console.error("❌ Erro ao enviar mensagem:", error);
            }
        });
    });
});
