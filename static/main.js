// const chatMessages = document.getElementById('chat-messages');
// const chatForm = document.getElementById('chat-form');
// const chatInput = document.getElementById('chat-input');
// const typingIndicator = document.getElementById('typing-indicator');

// // Helper: Scroll to bottom
// function scrollToBottom() {
//     chatMessages.scrollTop = chatMessages.scrollHeight;
// }

// // Helper: Create Message HTML
// function appendMessage(text, isUser = false) {
//     const div = document.createElement('div');
//     div.className = `flex items-start gap-2.5 ${isUser ? 'flex-row-reverse' : ''}`;
    
//     const avatarColor = isUser ? 'bg-gray-200 text-gray-600' : 'bg-leaf-100 text-leaf-600';
//     const icon = isUser ? 'fa-user' : 'fa-robot';
//     const align = isUser ? 'items-end' : 'items-start';
//     const bubbleColor = isUser ? 'bg-leaf-600 text-white rounded-s-xl rounded-ee-xl' : 'bg-white border-gray-200 text-gray-900 rounded-e-xl rounded-es-xl shadow-sm';
    
//     div.innerHTML = `
//         <div class="w-8 h-8 ${avatarColor} rounded-full flex items-center justify-center text-xs shrink-0">
//             <i class="fa-solid ${icon}"></i>
//         </div>
//         <div class="flex flex-col gap-1 w-full max-w-[320px] ${align}">
//             <div class="flex flex-col leading-1.5 p-3.5 border ${isUser ? 'border-transparent' : 'border-gray-200'} ${bubbleColor}">
//                 <p class="text-sm font-normal">${text}</p>
//             </div>
//             <span class="text-xs font-normal text-gray-400">Just now</span>
//         </div>
//     `;
    
//     chatMessages.appendChild(div);
//     scrollToBottom();
// }

// // Helper: Fill input from suggestion chips
// function fillInput(text) {
//     chatInput.value = text;
//     chatInput.focus();
// }

// // Logic: Reset Chat
// function resetChat() {
//     chatMessages.innerHTML = `
//         <div class="flex items-start gap-2.5">
//             <div class="w-8 h-8 bg-leaf-100 rounded-full flex items-center justify-center text-leaf-600 text-xs shrink-0">
//                 <i class="fa-solid fa-robot"></i>
//             </div>
//             <div class="flex flex-col gap-1 w-full max-w-[320px]">
//                 <div class="flex items-center space-x-2 rtl:space-x-reverse">
//                     <span class="text-sm font-semibold text-gray-900">NutriBot</span>
//                 </div>
//                 <div class="flex flex-col leading-1.5 p-4 border-gray-200 bg-white rounded-e-xl rounded-es-xl shadow-sm">
//                     <p class="text-sm font-normal text-gray-900">Hi there! 👋 I'm your personal nutrition assistant. Tell me what you ate today, or ask me for a healthy recipe!</p>
//                 </div>
//             </div>
//         </div>
//     `;
// }

// // Logic: Simulate AI Response
// function getBotResponse(userText) {
//     const text = userText.toLowerCase();
    
//     if (text.includes('hello') || text.includes('hi')) {
//         return "Hello! Ready to eat healthy today? 🍎";
//     }
//     if (text.includes('recipe') || text.includes('breakfast') || text.includes('dinner')) {
//         return "How about a Grilled Salmon with Quinoa and Asparagus? It's rich in Omega-3 and high protein! Would you like the full recipe?";
//     }
//     if (text.includes('calorie') || text.includes('fat') || text.includes('protein')) {
//         return "I can help calculate that. A medium banana usually has about 105 calories. Are you tracking macros today?";
//     }
//     if (text.includes('pizza') || text.includes('burger')) {
//         return "Tasty choice! Remember, balance is key. Maybe add a side salad to get some fiber? 🥗";
//     }
//     if (text.includes('avocado')) {
//         return "Yes! Avocado is a great source of healthy monounsaturated fats. It's high calorie but very nutritious.";
//     }
//     return "That sounds interesting! I'm learning more about nutrition every day. Could you tell me more about your diet goals?";
// }

// // Event: Handle Chat Submit
// async function handleChat(e) {
//     e.preventDefault();
//     const text = chatInput.value.trim();
//     if (!text) return;

//     // 1. Add User Message
//     appendMessage(text, true);
//     chatInput.value = '';

//     // 2. Show Typing Indicator
//     typingIndicator.classList.remove('hidden');
//     scrollToBottom();

//     // 3. Simulate Network Delay (1-2 seconds)
//     setTimeout(() => {
//         typingIndicator.classList.add('hidden');
        
//         // 4. Add Bot Response
//         const response = getBotResponse(text);
//         appendMessage(response, false);
//     }, 1500);
// }

document.addEventListener('DOMContentLoaded', () => {

    const chatMessages = document.getElementById('chat-messages');
    const chatForm = document.getElementById('chat-form');
    const chatInput = document.getElementById('chat-input');
    const typingIndicator = document.getElementById('typing-indicator');

    // Helper: Scroll to bottom
    function scrollToBottom() {
        chatMessages.scrollTop = chatMessages.scrollHeight;
    }

    // Helper: Create Message HTML
    function appendMessage(text, isUser = false) {
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

    // Helper: Fill input from suggestion chips
    window.fillInput = function(text) {
        chatInput.value = text;
        chatInput.focus();
    }

    // Logic: Reset Chat
    window.resetChat = function() {
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

    // Logic: Simulate AI Response
    function getBotResponse(userText) {
        const text = userText.toLowerCase();
        if (text.includes('hello') || text.includes('hi')) return "Hello! Ready to eat healthy today? 🍎";
        if (text.includes('recipe') || text.includes('breakfast') || text.includes('dinner')) return "How about a Grilled Salmon with Quinoa and Asparagus? It's rich in Omega-3 and high protein! Would you like the full recipe?";
        if (text.includes('calorie') || text.includes('fat') || text.includes('protein')) return "I can help calculate that. A medium banana usually has about 105 calories. Are you tracking macros today?";
        if (text.includes('pizza') || text.includes('burger')) return "Tasty choice! Remember, balance is key. Maybe add a side salad to get some fiber? 🥗";
        if (text.includes('avocado')) return "Yes! Avocado is a great source of healthy monounsaturated fats. It's high calorie but very nutritious.";
        return "That sounds interesting! I'm learning more about nutrition every day. Could you tell me more about your diet goals?";
    }

    // Event: Handle Chat Submit
    chatForm.addEventListener('submit', async (e) => {
        e.preventDefault();
        const text = chatInput.value.trim();
        if (!text) return;

        // 1. Add User Message
        appendMessage(text, true);
        chatInput.value = '';

        // 2. Show Typing Indicator
        typingIndicator.classList.remove('hidden');
        scrollToBottom();

        // 3. Simulate Network Delay
        setTimeout(() => {
            typingIndicator.classList.add('hidden');
            const response = getBotResponse(text);
            appendMessage(response, false);
        }, 1500);
    });

});
