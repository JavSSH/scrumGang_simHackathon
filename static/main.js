document.addEventListener('DOMContentLoaded', () => {
    const chatMessages = document.getElementById('chat-messages');
    const chatInput = document.getElementById('chat-input');
    const typingIndicator = document.getElementById('typing-indicator');

    // Helper: Scroll to bottom
    function scrollToBottom() {
        if (chatMessages) {
            chatMessages.scrollTop = chatMessages.scrollHeight;
        }
    }

    // Helper: Create Message HTML
    function appendMessage(text, isUser = false) {
        if (!chatMessages) return;

        const div = document.createElement('div');
        div.className = `flex items-start gap-2.5 ${isUser ? 'flex-row-reverse' : ''}`;
        
        const avatarColor = isUser ? 'bg-gray-200 text-gray-600' : 'bg-leaf-100 text-leaf-600';
        const icon = isUser ? 'fa-user' : 'fa-robot';
        const align = isUser ? 'items-end' : 'items-start';
        const bubbleColor = isUser ? 'bg-leaf-600 text-white rounded-s-xl rounded-ee-xl' : 'bg-white border-gray-200 text-gray-900 rounded-e-xl rounded-es-xl shadow-sm';
        
        div.innerHTML = `
            <div class="w-8 h-8 ${avatarColor} rounded-full flex items-center justify-center text-xs shrink-0">
                <i class="fa-solid ${icon}"></i>
            </div>
            <div class="flex flex-col gap-1 w-full max-w-[320px] ${align}">
                <div class="flex flex-col leading-1.5 p-3.5 border ${isUser ? 'border-transparent' : 'border-gray-200'} ${bubbleColor}">
                    <p class="text-sm font-normal">${text}</p>
                </div>
                <span class="text-xs font-normal text-gray-400">Just now</span>
            </div>
        `;
        
        chatMessages.appendChild(div);
        scrollToBottom();
    }

    // Main Chat Handler attached to the window object so HTML onsubmit can find it
    window.handleChat = async function(e) {
        e.preventDefault();
        const text = chatInput.value.trim();
        if (!text) return;

        // 1. Add User Message to UI
        appendMessage(text, true);
        chatInput.value = '';
        
        // 2. Show Typing Indicator
        if (typingIndicator) typingIndicator.classList.remove('hidden');
        scrollToBottom();

        try {
            // 3. Send to Python Backend
            const response = await fetch('/api/chat', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ message: text })
            });
            
            const data = await response.json();
            
            // 4. Show Bot Response
            if (typingIndicator) typingIndicator.classList.add('hidden');
            appendMessage(data.response, false);
            
        } catch (error) {
            console.error('Error:', error);
            if (typingIndicator) typingIndicator.classList.add('hidden');
            appendMessage("Sorry, I'm having trouble connecting to the server.", false);
        }
    };

    // Helper: Fill input from suggestion chips
    window.fillInput = function(text) {
        if (chatInput) {
            chatInput.value = text;
            chatInput.focus();
        }
    };
    
    // Reset Chat Function
    window.resetChat = function() {
        if (chatMessages) {
            chatMessages.innerHTML = `
                <div class="flex items-start gap-2.5">
                    <div class="w-8 h-8 bg-leaf-100 rounded-full flex items-center justify-center text-leaf-600 text-xs shrink-0">
                        <i class="fa-solid fa-robot"></i>
                    </div>
                    <div class="flex flex-col gap-1 w-full max-w-[320px]">
                        <div class="flex items-center space-x-2 rtl:space-x-reverse">
                            <span class="text-sm font-semibold text-gray-900">NutriBot</span>
                        </div>
                        <div class="flex flex-col leading-1.5 p-4 border-gray-200 bg-white rounded-e-xl rounded-es-xl shadow-sm">
                            <p class="text-sm font-normal text-gray-900">Hi there! 👋 I'm your personal nutrition assistant. Tell me what you ate today, or ask me for a healthy recipe!</p>
                        </div>
                    </div>
                </div>
            `;
        }
    };
});