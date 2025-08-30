export function EmptyQueryDialog({ isOpen, onClose }) {
  if (!isOpen) return null;

  return (
    <div className="fixed inset-0 flex items-center justify-center z-50 bg-black bg-opacity-30">
      <div className="bg-white rounded-2xl shadow-lg p-6 max-w-sm w-full text-center">
        <h2 className="text-lg font-semibold text-gray-800 mb-2">
          Please provide a query
        </h2>
        <p className="text-sm text-gray-500 mb-4">
          Enter a keyword to search for projects or users.
        </p>
        <button
          onClick={onClose}
          className="px-4 py-2 bg-black text-white rounded-2xl hover:bg-gray-800 transition"
        >
          OK
        </button>
      </div>
    </div>
  );
}
