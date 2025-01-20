import { useEffect, useState } from "react";
import styles from "../styles/Home.module.css";

export default function Welcome() {
  const [user, setUser] = useState(null);

  useEffect(() => {
    const fetchUserData = async () => {
      try {
        const response = await fetch("http://localhost:8000/auth/user", {
          credentials: "include",
        });
        const data = await response.json();
        console.log("data", data);

        if (data.user) {
          setUser(data.user);
        }
      } catch (error) {
        console.error("Error fetching user data:", error);
      }
    };

    fetchUserData();
  }, []);

  if (!user)
    return (
      <div className={styles.main}>
        <p>Loading...</p>
      </div>
    );

  return (
    <div className={styles.main}>
      <div>
        <p>Welcome,</p> <h2>{user.name}</h2>
      </div>
      <img src={user.picture} alt="User Avatar" />
      <p>email: {user.email}</p>

      <br />
      <br />

      <button
        onClick={async () => {
          await fetch("http://localhost:8000/logout", {
            method: "POST",
            credentials: "include",
          });
          window.location.href = "/";
        }}
      >
        Logout
      </button>
    </div>
  );
}
