$(document).ready(function() {
    const userId = $("#userId").val();  // ✅ Obtém o userId do HTML

    console.log("📡 Pusher iniciado para o utilizador ID:", userId);  // ✅ Debug inicial

    // Configurar Pusher
    const pusher = new Pusher("9505bbfcec175b686952", {
        cluster: "eu",
        encrypted: true
    });

    // Inscrever-se no canal privado do utilizador autenticado
    const channelName = `private-chat-${userId}`;
    console.log(`🔗 A inscrever-se no canal: ${channelName}`);  // ✅ Debug

    const channel = pusher.subscribe(channelName);

    // Verificar se o canal foi subscrito corretamente
    channel.bind("pusher:subscription_succeeded", function() {
        console.log(`✅ Ligado ao canal: ${channelName}`);
    });

    // Escutar eventos de novas mensagens e exibir no `chat-box`
    channel.bind("new-message", function(data) {
        console.log("📩 Nova mensagem recebida:", data);  // ✅ Debug no console
        $("#chat-box").append(`<p><strong>${data.sender_nome} ${data.sender_apelido}:</strong> ${data.message}</p>`);
        $("#chat-box").scrollTop($("#chat-box")[0].scrollHeight);  // ✅ Rola para a última mensagem
    });

    // Enviar mensagem via AJAX e adicioná-la imediatamente ao chat
    $("#chat-form").submit(function(event) {
        event.preventDefault();
        let receiverId = $("#receiver").val();
        let message = $("#message").val();

        console.log("✉️ A enviar mensagem:", message);  // ✅ Debug no console

        // Exibir mensagem imediatamente no chat
        $("#chat-box").append(`<p><strong>Você:</strong> ${message}</p>`);
        $("#chat-box").scrollTop($("#chat-box")[0].scrollHeight);

        $.ajax({
            type: "POST",
            url: "/chat/send_message/",
            contentType: "application/json",
            data: JSON.stringify({
                receiver_id: receiverId,
                message: message
            }),
            headers: { "X-CSRFToken": $("input[name=csrfmiddlewaretoken]").val() },
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
