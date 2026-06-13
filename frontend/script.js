async function searchVideos() {
    const query = document.getElementById("query").value.trim();
    const resultsDiv = document.getElementById("results");
    const statusDiv = document.getElementById("status");

    if (!query) {
        statusDiv.innerHTML = "Please enter a query.";
        return;
    }

    resultsDiv.innerHTML = "";
    statusDiv.innerHTML = "Searching...";
    statusDiv.classList.add("loading");

    try {
        const response = await fetch("http://127.0.0.1:8000/search", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ query: query })
        });

        if (!response.ok) {
            throw new Error(`HTTP Error: ${response.status}`);
        }

        const data = await response.json();

        statusDiv.classList.remove("loading");
        statusDiv.innerHTML = "";

        const results = data.video_results || [];
        const webResults = data.web_results || [];

        if (results.length === 0 && webResults.length === 0) {
            resultsDiv.innerHTML = `
                <div style="text-align: center; padding: 60px 20px; color: var(--text-secondary);">
                    <div style="font-size: 48px; margin-bottom: 16px;">🔍</div>
                    <p style="font-size: 16px;">No results found. Try a different search query.</p>
                </div>
            `;
            return;
        }

        let htmlContent = '';

        // Video Results Section
        if (results.length > 0) {
            htmlContent += '<div class="results-category">';
            htmlContent += '<h2 class="results-title">Video Results</h2>';
            htmlContent += '<div class="results-grid">';

            results.forEach((item, index) => {
                const result = item.result || item;
                const title = result.video_title || "Unknown Title";
                const chunk = result.chunk_text || "";

                htmlContent += `
                    <div class="result-card">
                        <div class="card-title">${index + 1}. ${title}</div>
                        <div class="card-preview">${chunk}</div>
                    </div>
                `;
            });

            htmlContent += '</div></div>';
        }

        // Web Results Section
        if (webResults.length > 0) {
            htmlContent += '<div class="results-category">';
            htmlContent += '<h2 class="results-title">Web Results</h2>';
            htmlContent += '<div class="results-grid web-results-grid">';

            webResults.slice(0, 5).forEach((web) => {
                const title = web.title || "No Title";
                const url = web.url || "#";
                const content = web.content || web.snippet || "No description available.";

                htmlContent += `
                    <div class="result-card">
                        <div class="card-title">${title}</div>
                        <a href="${url}" target="_blank" class="card-url">${url}</a>
                        <div class="card-preview">${content}</div>
                        <a href="${url}" target="_blank" class="card-action">
                            <span>🔗</span>
                            Visit Website
                        </a>
                    </div>
                `;
            });

            htmlContent += '</div></div>';
        }

        resultsDiv.innerHTML = htmlContent;

        // Scroll to results
        resultsDiv.scrollIntoView({ behavior: 'smooth', block: 'start' });

    } catch (error) {
        console.error("Search Error:", error);
        statusDiv.classList.remove("loading");
        statusDiv.innerHTML = `
            <div class="error-message">
                Error: ${error.message}
            </div>
        `;
    }
}

// Allow Enter key to search
document.addEventListener('DOMContentLoaded', function() {
    const queryInput = document.getElementById('query');
    queryInput.addEventListener('keypress', function(event) {
        if (event.key === 'Enter') {
            searchVideos();
        }
    });
});