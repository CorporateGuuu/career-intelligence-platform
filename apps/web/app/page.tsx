const metrics = [
  ["Applications", "42"],
  ["Responses", "19"],
  ["Interviews", "8"],
  ["Offers", "2"],
];

const events = [
  ["Oct 01", "Application detected", "Canonical"],
  ["Oct 01", "Acknowledgement classified", "Rules v1.0"],
  ["Oct 04", "Interview invitation", "Human verified"],
  ["Oct 08", "Resume v3 selected", "Linked"],
];

const skills = [
  ["Python", "matched"],
  ["FastAPI", "matched"],
  ["AWS", "matched"],
  ["Terraform", "matched"],
  ["Kubernetes", "gap"],
];

export default function Home() {
  return (
    <main className="shell">
      <header className="hero">
        <div>
          <p className="eyebrow">PORTFOLIO DEMO</p>
          <h1>Career Intelligence Platform</h1>
          <p className="lede">
            Deterministic application tracking with AI used for enrichment,
            resume matching, interview preparation, and follow-up—not as the
            authority over career history.
          </p>
        </div>
        <a
          className="github"
          href="https://github.com/CorporateGuuu/career-intelligence-platform"
        >
          View GitHub
        </a>
      </header>

      <section className="metrics">
        {metrics.map(([label, value]) => (
          <article className="metric" key={label}>
            <span>{label}</span>
            <strong>{value}</strong>
          </article>
        ))}
      </section>

      <section className="grid">
        <article className="panel">
          <p className="eyebrow">AUDITABLE STATE</p>
          <h2>Application event timeline</h2>
          <div className="timeline">
            {events.map(([date, name, source]) => (
              <div className="event" key={name}>
                <span>{date}</span>
                <div>
                  <strong>{name}</strong>
                  <p>{source}</p>
                </div>
              </div>
            ))}
          </div>
        </article>

        <article className="panel">
          <p className="eyebrow">AI RESUME COPILOT</p>
          <h2>Resume ↔ job match</h2>
          <div className="score">80%</div>
          <p className="muted">
            Example deterministic term coverage. AI recommendations remain
            advisory.
          </p>
          <div className="chips">
            {skills.map(([skill, state]) => (
              <span className={state} key={skill}>
                {skill}
              </span>
            ))}
          </div>
        </article>

        <article className="panel">
          <p className="eyebrow">HUMAN IN THE LOOP</p>
          <h2>Review queue</h2>
          <div className="review">
            <strong>Possible recruiter screen</strong>
            <p>
              Classification confidence is below the canonical acceptance
              threshold. A human can approve, correct, or reject the suggested
              event.
            </p>
            <div className="actions">
              <button>Approve</button>
              <button>Correct</button>
              <button>Reject</button>
            </div>
          </div>
        </article>

        <article className="panel">
          <p className="eyebrow">TRUST BOUNDARY</p>
          <h2>Canonical vs advisory</h2>
          <ul>
            <li><strong>Canonical:</strong> verified application events and corrections</li>
            <li><strong>Advisory:</strong> classifications, summaries, resume edits</li>
            <li><strong>Degraded safely:</strong> unconfigured Gmail/calendar/LLM providers</li>
          </ul>
        </article>
      </section>
    </main>
  );
}
