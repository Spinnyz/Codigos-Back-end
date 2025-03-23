
document.addEventListener('DOMContentLoaded', function() {

    initializeLikeButtons();
    

    initializeComments();
    
   
    initializeBookmarks();
    
 
    initializeFollowButtons();
    
    initializeSearch();
    
    initializePostAnalytics();
});


function initializeLikeButtons() {
    const likeButtons = document.querySelectorAll('.actions-left button:first-child');
    
    likeButtons.forEach(button => {
        button.addEventListener('click', function() {
            const post = this.closest('.post');
            

            const likesElement = post.querySelector('.likes strong');
            

            let likesCount = parseInt(likesElement.textContent);
            

            const img = this.querySelector('img');
            if (img.src.includes('like--v1.png')) {
 
                img.src = 'https://img.icons8.com/ios-filled/50/FF3040/like--v1.png';
                img.style.filter = 'none';
                likesCount++;
                

                const heart = document.createElement('div');
                heart.classList.add('heart-animation');
                post.querySelector('.post-content').appendChild(heart);
                

                setTimeout(() => {
                    heart.remove();
                }, 1000);
            } else {
                img.src = 'https://img.icons8.com/ios/50/000000/like--v1.png';
                img.style.filter = '';
                likesCount--;
            }
            

            likesElement.textContent = likesCount + (likesCount === 1 ? ' curtida' : ' curtidas');
        });
    });
}




function initializeComments() {
    const commentForms = document.querySelectorAll('.add-comment');
    
    commentForms.forEach(form => {
        const input = form.querySelector('input');
        const button = form.querySelector('button');
        

        input.addEventListener('input', function() {
            button.style.opacity = this.value.trim() ? '1' : '0.5';
        });
        

        button.addEventListener('click', function() {
            const commentText = input.value.trim();
            if (!commentText) return;
            

            const post = this.closest('.post');

            const commentsContainer = post.querySelector('.comments');

            const newComment = document.createElement('p');
            newComment.innerHTML = `<strong>seu_usuario</strong> ${commentText}`;
  
            commentsContainer.appendChild(newComment);
            
        
            const commentsCountElement = post.querySelector('.comments-count');
            const currentCount = parseInt(commentsCountElement.textContent.match(/\d+/)[0]);
            commentsCountElement.textContent = `Ver todos os ${currentCount + 1} comentários`;
           
            input.value = '';
            button.style.opacity = '0.5';
    
            showNotification('Comentário adicionado!');
        });
    });
}


function initializeBookmarks() {
    const bookmarkButtons = document.querySelectorAll('.actions-right button');
    
    bookmarkButtons.forEach(button => {
        button.addEventListener('click', function() {

            const img = this.querySelector('img');
            if (img.src.includes('bookmark-ribbon--v1.png')) {
  
                img.src = 'https://img.icons8.com/ios-filled/50/000000/bookmark-ribbon--v1.png';
                showNotification('Post salvo em sua coleção');
            } else {

                img.src = 'https://img.icons8.com/ios/50/000000/bookmark-ribbon--v1.png';
                showNotification('Post removido de sua coleção');
            }
        });
    });
}

/**
 * Handle follow buttons
 */
function initializeFollowButtons() {
    const followButtons = document.querySelectorAll('.follow-link');
    
    followButtons.forEach(button => {
        button.addEventListener('click', function(e) {
            e.preventDefault();
            
            // Toggle follow state
            if (this.textContent === 'Seguir') {
                this.textContent = 'Seguindo';
                this.style.color = '#262626';
                this.style.fontWeight = '400';
                
                // Get username from the suggestion item
                const username = this.closest('.suggestion-item').querySelector('h5').textContent;
                showNotification(`Agora você está seguindo ${username}`);
            } else {
                this.textContent = 'Seguir';
                this.style.color = '#0095f6';
                this.style.fontWeight = '600';
            }
        });
    });
}


/**
 * Initialize post analytics and tracking
 */
function initializePostAnalytics() {
    const posts = document.querySelectorAll('.post');
    
    posts.forEach(post => {
        // Track post views
        const observer = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    // Post is visible in viewport
                    // In a real application, you would send this data to your analytics service
                    console.log('Post view:', post.querySelector('.user-info h2').textContent);
                    observer.unobserve(entry.target);
                }
            });
        }, { threshold: 0.5 }); // Post is considered viewed when 50% visible
        
        observer.observe(post);
        
        // Track engagement (all clicks on post)
        post.addEventListener('click', function(e) {
            // In a real application, you would track different types of engagement
            const target = e.target.closest('button');
            if (target) {
                const action = target.querySelector('img')?.alt || 'interaction';
                console.log('Post engagement:', post.querySelector('.user-info h2').textContent, action);
            }
        });
    });
}


function showNotification(message) {

    const notification = document.createElement('div');
    notification.classList.add('notification');
    notification.textContent = message;

    document.body.appendChild(notification);
    
    // Show notification with animation
    setTimeout(() => {
        notification.classList.add('show');
    }, 10);
    
    // Remove after display time
    setTimeout(() => {
        notification.classList.remove('show');
        setTimeout(() => {
            notification.remove();
        }, 300);
    }, 3000);
}

// Add CSS for new elements created by JS
const styleSheet = document.createElement('style');
styleSheet.textContent = `
    .heart-animation {
        position: absolute;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
        width: 100px;
        height: 100px;
        background-image: url('https://img.icons8.com/ios-filled/100/FF3040/like--v1.png');
        background-size: contain;
        background-repeat: no-repeat;
        background-position: center;
        opacity: 0;
        animation: heart-pulse 1s ease-in-out;
    }
    
    @keyframes heart-pulse {
        0% { opacity: 0; transform: translate(-50%, -50%) scale(0.1); }
        15% { opacity: 1; }
        30% { transform: translate(-50%, -50%) scale(1.2); }
        45% { transform: translate(-50%, -50%) scale(0.8); }
        60% { transform: translate(-50%, -50%) scale(1.1); }
        100% { opacity: 0; transform: translate(-50%, -50%) scale(1); }
    }
    
    .notification {
        position: fixed;
        bottom: -50px;
        left: 50%;
        transform: translateX(-50%);
        background-color: #262626;
        color: white;
        padding: 12px 20px;
        border-radius: 8px;
        font-size: 14px;
        z-index: 1000;
        transition: bottom 0.3s ease-in-out;
        box-shadow: 0 2px 10px rgba(0, 0, 0, 0.3);
    }
    
    .notification.show {
        bottom: 20px;
    }
    
    .search-dropdown {
        position: absolute;
        top: 45px;
        left: 0;
        width: 375px;
        background-color: white;
        border-radius: 4px;
        box-shadow: 0 0 5px rgba(0, 0, 0, 0.2);
        z-index: 10;
    }
    
    .search-dropdown-header {
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 12px 16px;
        border-bottom: 1px solid #dbdbdb;
    }
    
    .search-dropdown-header h4 {
        font-size: 16px;
        font-weight: 600;
    }
    
    .search-dropdown-header button {
        color: #0095f6;
        font-weight: 600;
        font-size: 14px;
    }
    
    .search-results {
        max-height: 375px;
        overflow-y: auto;
    }
    
    .search-result-item {
        display: flex;
        align-items: center;
        padding: 8px 16px;
        cursor: pointer;
    }
    
    .search-result-item:hover {
        background-color: #fafafa;
    }
    
    .no-results {
        padding: 16px;
        text-align: center;
        color: #8e8e8e;
    }
`;
document.head.appendChild(styleSheet);
