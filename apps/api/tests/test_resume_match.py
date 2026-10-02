from app.domain.resume import match_resume


def test_resume_match_is_reproducible():
    resume = "Python FastAPI AWS Terraform PostgreSQL"
    job = "Seeking Python FastAPI AWS Kubernetes Terraform"

    first = match_resume(resume, job)
    second = match_resume(resume, job)

    assert first == second
    assert "python" in first.matched_terms
    assert "kubernetes" in first.missing_terms
    assert 0.0 < first.score < 1.0


def test_empty_job_description_returns_zero_score():
    result = match_resume("Python FastAPI", "")

    assert result.score == 0.0
    assert result.matched_terms == []
    assert result.missing_terms == []
