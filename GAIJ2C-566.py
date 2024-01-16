Generate Code for this requirement: Response:
package model
import "github.com/jinzhu/gorm"

// User is a schema for the `users` table.
type User struct {
	gorm.Model
	Name     string `json:"name,omitempty"` // Name of the user.
	Email    string `json:"email,omitempty"` // Email address of the user.
	Picture  string `json:"picture,omitempty"` // URL of the profile picture.
	Bio      string `json:"bio,omitempty"` // Short bio of the user.
	Location string `json:"location,omitempty"` // Location of the user.
}

func (u *User) CreateUser(db *gorm.DB) error {
	// Save the user to the database.
	err := db.Save(u).Error
	if err!= nil {
		return err
	}

	return nil
}

func (u *User) SaveProfile(db *gorm.DB) error {
	// Save the user's profile information.
	err := db.Model(u).UpdateColumn("name", u.Name).UpdateColumn("email", u.Email).UpdateColumn("bio", u.Bio).UpdateColumn("location", u.Location).Error
	if err!= nil {
		return err
	}

	return nil
}

func (u *User) CreateUserAndSave(db *gorm.DB) error {
	// First, create a new user with the default values.
	u.Name = "Your Name"
	u.Email = "your.email@example.com"

	// Then, save the user to the database.
