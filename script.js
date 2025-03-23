// script.js

// Função para curtir um post
function likePost(post) {
    const likeButton = post.querySelector('.actions-left button');
    const likeIcon = likeButton.querySelector('img');
    const likesCount = post.querySelector('.likes strong');

    likeButton.addEventListener('click', () => {
        let likes = parseInt(likesCount.textContent);

        // Alternar entre curtido e não curtido
        if (likeButton.classList.contains('liked')) {
            likes--;
            likeButton.classList.remove('liked');
            likeIcon.src = "https://img.icons8.com/ios/50/000000/like--v1.png"; // Ícone normal
        } else {
            likes++;
            likeButton.classList.add('liked');
            likeIcon.src = "https://img.icons8.com/ios-filled/50/000000/like.png"; // Ícone curtido
        }

        likesCount.textContent = likes + ' curtidas';

        // Adiciona uma animação de like
        likeButton.classList.add('like-animation');
        setTimeout(() => {
            likeButton.classList.remove('like-animation');
        }, 300);
    });
}

// Função para adicionar um comentário
function addComment(post) {
    const commentInput = post.querySelector('.add-comment input');
    const commentButton = post.querySelector('.add-comment button');
    const commentsSection = post.querySelector('.comments');
    const commentsCount = post.querySelector('.comments-count');

    commentButton.addEventListener('click', () => {
        const commentText = commentInput.value.trim();
        if (commentText !== '') {
            // Cria um novo comentário
            const newComment = document.createElement('p');
            newComment.textContent = commentText;
            newComment.classList.add('comment-animation'); // Adiciona animação
            commentsSection.appendChild(newComment);

            // Atualiza o contador de comentários
            const currentCount = parseInt(commentsCount.textContent.replace(/\D/g, ''));
            commentsCount.textContent = `Ver todos os ${currentCount + 1} comentários`;

            // Limpa o campo de comentário
            commentInput.value = '';

            // Remove a animação após 300ms
            setTimeout(() => {
                newComment.classList.remove('comment-animation');
            }, 300);
        }
    });
}

// Função para seguir um usuário
function followUser(followButton) {
    followButton.addEventListener('click', () => {
        if (followButton.textContent === 'Seguir') {
            followButton.textContent = 'Seguindo';
            followButton.classList.add('follow-animation'); // Adiciona animação
            setTimeout(() => {
                followButton.classList.remove('follow-animation');
            }, 300);
        } else {
            followButton.textContent = 'Seguir';
        }
    });
}

// Aplicar as funções a todos os posts
document.querySelectorAll('.post').forEach(post => {
    likePost(post);
    addComment(post);
});

// Aplicar a função de seguir a todos os botões de seguir
document.querySelectorAll('.follow-link').forEach(followButton => {
    followUser(followButton);
});

// Função para mostrar/ocultar opções de post
document.querySelectorAll('.more-options').forEach(button => {
    button.addEventListener('click', () => {
        alert('Opções do post clicadas!');
        // Aqui você pode adicionar mais funcionalidades, como abrir um menu de opções
    });
});