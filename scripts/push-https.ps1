git remote set-url origin "https://$($env:GITHUB_TOKEN)@github.com/IfIknewher/twoboysAB.git"
git add .
git commit -m "Automated push" 2>$null
git push origin $(git rev-parse --abbrev-ref HEAD)
