import { useState } from "react";
import { useDispatch, useSelector } from "react-redux";
import { searchProjects, searchUsers } from "../services/api";
import { EmptyQueryDialog } from "./AlertDialog";
function Badge({ children }) {
  return (
    <span className="px-2 py-1 text-xs rounded-full border shadow-sm">
      {children}
    </span>
  );
}
function SearchBar({ mode, setMode }) {
  const dispatch = useDispatch();
  const { loading, p } = useSelector((s) => s.search);

  const [q, setQ] = useState("");
  const [isOpen, openDialog] = useState(false);

  const onSubmit = (e) => {
    e.preventDefault();
    if (!q.trim()) {
      openDialog(true);
      return;
    }
    if (mode === "projects") dispatch(searchProjects(q));
    else dispatch(searchUsers(q));
  };

  return (
    <div className="flex flex-col items-center gap-3">
      <EmptyQueryDialog isOpen={isOpen} onClose={() => openDialog(false)} />
      <div className="flex gap-2">
        <button
          className={`px-4 py-2 rounded-2xl ${
            mode === "projects" ? "bg-black text-white" : "bg-gray-200"
          }`}
          onClick={() => dispatch(setMode("projects"))}
        >
          Search Projects
        </button>
        <button
          className={`px-4 py-2 rounded-2xl ${
            mode === "users" ? "bg-black text-white" : "bg-gray-200"
          }`}
          onClick={() => dispatch(setMode("users"))}
        >
          Search Users
        </button>
      </div>
      <form
        onSubmit={onSubmit}
        className="w-full md:max-w-xl mx-auto flex gap-2"
      >
        <input
          className="flex-1 border rounded-2xl px-4 py-2 focus:outline-none focus:ring"
          placeholder={`Search ${mode} by skill e.g. django, flutter`}
          value={q}
          onChange={(e) => setQ(e.target.value)}
        />
        <button
          type="submit"
          disabled={loading}
          className="rounded-2xl px-4 py-2 bg-black text-white disabled:opacity-50"
        >
          {loading ? "Searching…" : "Search"}
        </button>
      </form>
    </div>
  );
}

function ProjectCard({ p }) {
  const skills = p.skills || [];
  return (
    <div className="rounded-2xl border p-4 bg-white shadow-sm">
      <h3 className="font-semibold text-lg">{p.title}</h3>
      <p className="text-sm text-gray-600 line-clamp-3">{p.description}</p>
      <div className="flex flex-wrap gap-2 mt-2">
        {skills.map((s, i) => (
          <Badge key={i}>{s}</Badge>
        ))}
      </div>
      {p.link && (
        <a
          href={p.link}
          target="_blank"
          rel="noreferrer"
          className="text-sm underline mt-2 block"
        >
          View
        </a>
      )}
    </div>
  );
}

export function UserCard({ u }) {
  if (!u) {
    console.log("UserCard: no user passed");
    return null;
  }
  console.log("from card", u);

  const skills = u.skills_display || [];
  const projects = u.projects || [];
  const work = u.work || [];
  return (
    <div className="rounded-2xl border sm:p-5 w-min p-2 bg-white shadow-sm space-y-3">
      <div className="flex items-center justify-between">
        <div>
          <h3 className="text-lg font-semibold">{u.full_name}</h3>
          <p className="text-sm text-gray-600">{u.email}</p>
          {u.education && (
            <p className="text-sm text-gray-600 mt-1">{u.education}</p>
          )}
        </div>
        <div className="flex gap-3">
          {u.github && (
            <a
              href={u.github}
              target="_blank"
              rel="noreferrer"
              className="underline text-sm"
            >
              GitHub
            </a>
          )}
          {u.linkedin && (
            <a
              href={u.linkedin}
              target="_blank"
              rel="noreferrer"
              className="underline text-sm"
            >
              LinkedIn
            </a>
          )}
          {u.portfolio && (
            <a
              href={u.portfolio}
              target="_blank"
              rel="noreferrer"
              className="underline text-sm"
            >
              Portfolio
            </a>
          )}
        </div>
      </div>

      {u.bio && <p className="text-sm text-gray-700">{u.bio}</p>}

      {skills.length > 0 && (
        <div className="flex flex-wrap gap-2">
          {skills.map((s, i) => (
            <Badge key={i}>{s}</Badge>
          ))}
        </div>
      )}

      {projects.length > 0 && (
        <div className="mt-3">
          <h4 className="font-semibold text-sm">Projects:</h4>
          <ul className="list-disc list-inside text-sm text-gray-600">
            {projects.map((p) => (
              <li key={p.id}>
                <span className="font-medium">{p.title}</span> –{" "}
                {p.description?.substring(0, 60)}…
              </li>
            ))}
          </ul>
        </div>
      )}

      {work.length > 0 && (
        <div className="mt-3">
          <h4 className="font-semibold text-sm">Work Experience:</h4>
          <ul className="list-disc list-inside text-sm text-gray-600">
            {work.map((w) => (
              <li key={w.id}>
                <span className="font-medium">{w.company}</span> – {w.role} (
                {w.start_date} to {w.end_date || "Present"})
              </li>
            ))}
          </ul>
        </div>
      )}
    </div>
  );
}

function Results({ mode }) {
  const { items, loading, error, t } = useSelector((s) => s.search);

  if (loading) return <p className="text-center mt-6">Loading…</p>;
  if (error) return <p className="text-center mt-6 text-red-600">{error}</p>;

  if (!items || !items.length)
    return <p className="text-center mt-6">No results found.</p>;
  const isProject = items[0].title !== undefined;
  const isUser = items[0].full_name !== undefined;
  return (
    <div className="grid gap-4 sm:grid-cols-2 lg:grid-cols-3 mt-6">
      {mode === "projects" && isProject ? (
        items.map((p) => <ProjectCard key={p.id} p={p} />)
      ) : mode === "users" && isUser ? (
        items.map((u) => <UserCard key={u.id} u={u} />)
      ) : (
        <p className="text-center mt-6">No results found please search !</p>
      )}
    </div>
  );
}

export default function Shell() {
  const API_BASE_URL =
    import.meta.env.FRONTEND_BASE_URL ||
    "https://manizh.pythonanywhere.com/api";
  const [mode, setMode] = useState("projects");
  return (
    <div className="min-h-screen bg-gray-50">
      <header className="sticky top-0 backdrop-blur bg-white/80 border-b">
        <div className="max-w-6xl mx-auto px-4 py-3 flex items-center justify-between">
          <h1 className="text-xl font-bold">Me Api</h1>
          <div className="text-xs text-gray-500">API: {API_BASE_URL}</div>
        </div>
      </header>

      <main className="max-w-6xl mx-auto px-4 py-6">
        <div className="rounded-2xl border p-4 bg-white shadow-sm">
          <SearchBar mode={mode} setMode={setMode} />
        </div>

        <Results mode={mode} setMode={setMode} />
      </main>

      <footer className="text-center text-xs text-gray-500 py-6">
        Built with React + Tailwind + Axios + Redux Toolkit + Django + Drf +
        Mysql
      </footer>
    </div>
  );
}
